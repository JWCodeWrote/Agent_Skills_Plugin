#!/usr/bin/env python3
"""Close Gemini and Qwen pages via Chrome CDP without closing the entire browser.

Usage:
    python3 close_ai_pages.py
"""
import json
import subprocess
import asyncio

try:
    import websockets
except ImportError:
    print("Error: websockets module not found. Install with: pip install websockets")
    exit(1)


async def close_page(browser_ws_url: str, target_id: str) -> bool:
    """Close a specific page/tab identified by target_id."""
    try:
        async with websockets.connect(browser_ws_url) as ws:
            await ws.send(json.dumps({
                "id": 1,
                "method": "Target.closeTarget",
                "params": {"targetId": target_id}
            }))
            response = await ws.recv()
            result = json.loads(response)
            return result.get("result", {}).get("success", False)
    except Exception as e:
        print(f"Error closing page: {e}")
        return False


def get_pages() -> list:
    """Get list of open pages from CDP."""
    result = subprocess.run(
        ["curl", "-s", "http://localhost:9222/json"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return []
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return []


def get_browser_ws_url() -> str | None:
    """Get the browser-level WebSocket URL for CDP commands."""
    result = subprocess.run(
        ["curl", "-s", "http://localhost:9222/json/version"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return None
    try:
        data = json.loads(result.stdout)
        return data.get("webSocketDebuggerUrl")
    except json.JSONDecodeError:
        return None


def main():
    # Check CDP is running
    pages = get_pages()
    if not pages:
        print("Error: Cannot connect to Chrome CDP on port 9222.")
        print("Make sure Chrome is running with --remote-debugging-port=9222")
        return 1

    browser_ws = get_browser_ws_url()
    if not browser_ws:
        print("Error: Cannot get browser WebSocket URL.")
        return 1

    # Find AI pages to close
    ai_hosts = ["gemini.google.com", "chat.qwen.ai"]
    pages_to_close = []

    for page in pages:
        if page.get("type") != "page":
            continue
        url = page.get("url", "")
        for host in ai_hosts:
            if host in url:
                pages_to_close.append({
                    "id": page.get("id"),
                    "url": url
                })
                break

    if not pages_to_close:
        print("No Gemini or Qwen pages found.")
        return 0

    # Close each AI page
    for page in pages_to_close:
        print(f"Closing: {page['url']}")
        success = asyncio.run(close_page(browser_ws, page["id"]))
        if success:
            print(f"  ✓ Closed successfully")
        else:
            print(f"  ✗ Failed to close")

    print(f"\nClosed {len(pages_to_close)} AI page(s). Chrome is still running.")
    return 0


if __name__ == "__main__":
    exit(main())
