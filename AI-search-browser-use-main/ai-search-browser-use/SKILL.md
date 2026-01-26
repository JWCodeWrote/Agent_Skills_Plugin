---
name: ai-search-browser-use
description: Use this skill when a task needs AI-assisted web research via a real browser. Uses Chrome CDP (Chrome DevTools Protocol) as the primary automation method, with browser-use as fallback. Supports Gemini + Qwen queries with consolidated answers and citations.
---

# AI Search Browser Use

## Overview

Enable reliable AI-assisted web research by using **Chrome CDP** as the primary automation method. This approach connects to a Chrome instance with remote debugging enabled, allowing direct control over browser tabs for Gemini + Qwen queries.

**Key Advantage**: CDP uses your logged-in Chrome profile, so no additional authentication is needed for Gemini and Qwen.

## Workflow

### 0) Check Prerequisites

**Required: Python + websockets**

```bash
python3 --version
python3 -m pip show websockets
```

If `websockets` is missing, install in a venv:

```bash
python3 -m venv .venv
./.venv/bin/pip install websockets
```

**Required: Google Chrome**

Verify Chrome is installed:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --version
```

If not installed:

- macOS: `brew install --cask google-chrome`
- Windows: `winget install --id Google.Chrome -e`

### 1) Launch Chrome with CDP (Remote Debugging)

**CRITICAL**: CDP requires a **non-default user data directory**. This serves two purposes:

1. **Allows running alongside your normal Chrome**: By using a separate `--user-data-dir`, the CDP Chrome runs as an independent process. You can continue using your regular Chrome without any conflicts.
2. **Preserves login state**: By cloning your existing Chrome profile, the CDP Chrome inherits your logged-in sessions for Gemini, Qwen, and other sites.

**Clone your existing Chrome profile**:

```bash
# Clean and clone profile (only needed once, or when login expires)
rm -rf /tmp/chrome-ai-profile
rsync -a "$HOME/Library/Application Support/Google/Chrome/" /tmp/chrome-ai-profile/

# Launch CDP Chrome (runs independently from your normal Chrome!)
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="/tmp/chrome-ai-profile" \
  "https://gemini.google.com/app" "https://chat.qwen.ai/" &
```

> **Note**: You will see two Chrome icons in your dock - one is your normal Chrome, the other is the CDP instance.

**For Windows**:

```powershell
# Clone profile
Remove-Item -Recurse -Force "$env:TEMP\chrome-ai-profile" -ErrorAction SilentlyContinue
Copy-Item -Recurse "$env:LOCALAPPDATA\Google\Chrome\User Data" "$env:TEMP\chrome-ai-profile"

# Launch Chrome with remote debugging
Start-Process "chrome.exe" -ArgumentList "--remote-debugging-port=9222", "--user-data-dir=$env:TEMP\chrome-ai-profile", "https://gemini.google.com/app", "https://chat.qwen.ai/"
```

### 2) Verify CDP Connection

Confirm Chrome is listening on the debugging port:

```bash
curl -s http://localhost:9222/json | python3 -m json.tool
```

You should see a JSON array containing page entries for both `gemini.google.com` and `chat.qwen.ai`:

```json
[
  {
    "type": "page",
    "url": "https://gemini.google.com/app",
    "webSocketDebuggerUrl": "ws://localhost:9222/devtools/page/..."
  },
  {
    "type": "page",
    "url": "https://chat.qwen.ai/",
    "webSocketDebuggerUrl": "ws://localhost:9222/devtools/page/..."
  }
]
```

### 3) Run AI Queries via CDP

Use the CDP Query Script to send queries to both AI engines:

**ai_query.py**:

```python
import asyncio
import websockets
import json
import subprocess
import sys

def find_page(pages, host):
    for page in pages:
        if page.get("type") == "page" and host in page.get("url", ""):
            return page
    return None

async def send_query(ws_url, query_text, wait_seconds=30):
    async with websockets.connect(ws_url) as ws:
        input_js = f"""
        (function() {{
            const editor = document.querySelector('div[contenteditable="true"]') || document.querySelector('textarea');
            if (editor) {{
                editor.focus();
                document.execCommand('insertText', false, `{query_text}`);
                editor.dispatchEvent(new Event('input', {{bubbles: true}}));
                return 'input-ok';
            }}
            return 'editor-not-found';
        }})()
        """
        await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": input_js}}))
        await ws.recv()

        click_js = """
        (function() {
            const btn = document.querySelector('button[aria-label*="傳送"]')
                     || document.querySelector('button[aria-label*="Send"]')
                     || document.querySelector('button[type="submit"]');
            if (btn) { btn.click(); return 'clicked'; }
            return 'button-not-found';
        })()
        """
        await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": click_js}}))
        await ws.recv()

        await asyncio.sleep(wait_seconds)

        extract_js = """
        (function() {
            const md = document.querySelectorAll('.markdown');
            if (md.length > 0) return md[md.length - 1].innerText;
            return 'No response found';
        })()
        """
        await ws.send(json.dumps({"id": 3, "method": "Runtime.evaluate", "params": {"expression": extract_js}}))
        response = await ws.recv()
        result = json.loads(response)
        return result.get("result", {}).get("result", {}).get("value", "No content")

async def main(query):
    result = subprocess.run(["curl", "-s", "http://localhost:9222/json"], capture_output=True, text=True)
    pages = json.loads(result.stdout)

    gemini = find_page(pages, "gemini.google.com")
    qwen = find_page(pages, "chat.qwen.ai")
    if not gemini or not qwen:
        print("Error: Gemini or Qwen page not found.")
        return

    g = await send_query(gemini["webSocketDebuggerUrl"], query)
    q = await send_query(qwen["webSocketDebuggerUrl"], query)

    print("GEMINI RESPONSE:\\n" + g)
    print("\\n" + "=" * 50 + "\\n")
    print("QWEN RESPONSE:\\n" + q)

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "請用繁體中文回答：什麼是區塊鏈？"
    asyncio.run(main(query))
```

Run:

```bash
python3 ai_query.py "你的查詢問題"
```

### 4) Synthesize and Cite Results

- Consolidate results from Gemini and Qwen into a single, coherent answer.
- Highlight consensus points first, then disagreements or uncertainties.
- Provide citations for each major claim using this format:
  - `Source Title — Domain — URL`
- If the AI answers do not provide sources, open the referenced sites and cite the primary sources directly.

### 5) Close AI Pages (Recommended) or Chrome Instance

After completing the task, you have two options:

#### Option A: Close only the AI pages (keep Chrome running)

Use CDP to close only the Gemini and Qwen tabs, keeping the Chrome instance running for other tasks:

**close_ai_pages.py**:

```python
import json
import subprocess
import asyncio
import websockets

async def close_page(browser_ws_url, target_id):
    async with websockets.connect(browser_ws_url) as ws:
        await ws.send(json.dumps({
            "id": 1,
            "method": "Target.closeTarget",
            "params": {"targetId": target_id}
        }))
        await ws.recv()

def main():
    result = subprocess.run(["curl", "-s", "http://localhost:9222/json"], capture_output=True, text=True)
    pages = json.loads(result.stdout)

    # Get browser WebSocket URL
    version = subprocess.run(["curl", "-s", "http://localhost:9222/json/version"], capture_output=True, text=True)
    browser_ws = json.loads(version.stdout).get("webSocketDebuggerUrl")

    for page in pages:
        url = page.get("url", "")
        if "gemini.google.com" in url or "chat.qwen.ai" in url:
            target_id = page.get("id")
            print(f"Closing: {url}")
            asyncio.run(close_page(browser_ws, target_id))

if __name__ == "__main__":
    main()
```

Run:

```bash
python3 close_ai_pages.py
```

Or use a quick one-liner (bash + Python):

```bash
# Get page IDs and close them
curl -s http://localhost:9222/json | python3 -c "
import json, sys, subprocess, asyncio, websockets

pages = json.load(sys.stdin)
version = json.loads(subprocess.run(['curl', '-s', 'http://localhost:9222/json/version'], capture_output=True, text=True).stdout)
browser_ws = version.get('webSocketDebuggerUrl')

async def close(browser_ws, tid, url):
    async with websockets.connect(browser_ws) as ws:
        await ws.send(json.dumps({'id': 1, 'method': 'Target.closeTarget', 'params': {'targetId': tid}}))
        await ws.recv()
        print(f'Closed: {url}')

for p in pages:
    url = p.get('url', '')
    if 'gemini.google.com' in url or 'chat.qwen.ai' in url:
        asyncio.run(close(browser_ws, p['id'], url))
"
```

#### Option B: Close the entire CDP Chrome instance

If you want to close the entire Chrome instance (releases port 9222):

```bash
# macOS
pkill -f "Google Chrome.*--remote-debugging-port=9222"
```

```powershell
# Windows
Get-Process chrome | Where-Object {$_.CommandLine -match "remote-debugging-port=9222"} | Stop-Process -Force
```

---

## CDP Troubleshooting

| Problem                                                           | Cause                                             | Solution                                                     |
| ----------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------ |
| `curl: (7) Failed to connect`                                     | Chrome not running with `--remote-debugging-port` | Re-launch Chrome with the CDP flags                          |
| WebSocket connection refused                                      | Page ID changed                                   | Re-fetch `http://localhost:9222/json` for new WebSocket URLs |
| `editor not found`                                                | Page not fully loaded                             | Wait a few seconds and retry                                 |
| Login page instead of `/app`                                      | Profile lacks login state                         | Re-clone a properly logged-in Chrome profile                 |
| `DevTools remote debugging requires a non-default data directory` | Using default profile                             | Always use `/tmp/chrome-ai-profile` or custom path           |
| Port 9222 already in use                                          | Previous CDP instance not closed                  | Kill the previous instance first                             |

---

## Best Practices

1. **Always use CDP as the primary method** for authenticated queries.
2. **Clone the profile each time** to ensure a fresh, logged-in state.
3. **Wait longer for complex prompts** (30–60 seconds).
4. **Close the CDP Chrome instance after use** to release port 9222.
5. **Update the cloned profile** if login expires.

---

## Fallback: browser-use

If CDP is unavailable (e.g., Chrome not installed, or CDP setup fails), use `browser-use` as a fallback:

### Install browser-use

```bash
brew install pipx
pipx install browser-use
pipx ensurepath
```

Restart the terminal after `pipx ensurepath` to load PATH changes.

### Launch with browser-use

```bash
browser-use --browser real open "https://gemini.google.com/app"
browser-use --browser real open "https://chat.qwen.ai/"
```

### Close browser-use session

```bash
browser-use close
```

**Note**: When using browser-use as a fallback, clearly document this in your outputs. Do not claim CDP was used if it was not.

---

## Browser Selection (Optional)

Run `scripts/browser_plan.py --json` to detect OS, find installed browsers, and get open/close commands:

```bash
python3 scripts/browser_plan.py --json
```

For custom browser paths, set `BROWSER_PATH_OVERRIDES`:

```bash
BROWSER_PATH_OVERRIDES='{"quark":["/Custom/Path/Quark.app"]}' python3 scripts/browser_plan.py --json
```

---

## Outputs

- Final answer with integrated reasoning from Gemini and Qwen.
- Explicit citations showing where each major claim was found.
- Clear indication of which automation method was used (CDP or browser-use fallback).

## Resources

- `scripts/browser_plan.py`: Detect OS, select browser, and provide open/close/install commands.
- `references/ai_search_targets.md`: Public entry points for Gemini/Qwen and citation guidance.
