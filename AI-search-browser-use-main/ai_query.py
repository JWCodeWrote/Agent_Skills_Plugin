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


async def send_query(ws_url, query_text, wait_seconds=40):
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

    print("GEMINI RESPONSE:\n" + g)
    print("\n" + "=" * 50 + "\n")
    print("QWEN RESPONSE:\n" + q)


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "請用繁體中文回答：什麼是區塊鏈？"
    asyncio.run(main(query))
