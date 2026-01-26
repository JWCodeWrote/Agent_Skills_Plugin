#!/usr/bin/env python3
"""Plan browser usage with OS detection and fallback selection.

Outputs either human-readable steps or JSON when --json is passed.
"""
from __future__ import annotations

import argparse
import json
import os
import platform
from pathlib import Path


def _is_windows() -> bool:
    return platform.system().lower().startswith("win")


def _is_macos() -> bool:
    return platform.system().lower() == "darwin"


def _expand_paths(paths: list[str]) -> list[str]:
    expanded: list[str] = []
    for p in paths:
        expanded.append(os.path.expandvars(os.path.expanduser(p)))
    return expanded


def _default_browser_paths() -> dict[str, list[str]]:
    if _is_macos():
        return {
            "chrome": [
                "/Applications/Google Chrome.app",
                "~/Applications/Google Chrome.app",
            ],
            "quark": [
                "/Applications/Quark.app",
                "~/Applications/Quark.app",
            ],
        }
    if _is_windows():
        pf = os.environ.get("ProgramFiles", r"C:\\Program Files")
        pf86 = os.environ.get("ProgramFiles(x86)", r"C:\\Program Files (x86)")
        lad = os.environ.get("LocalAppData", r"C:\\Users\\%USERNAME%\\AppData\\Local")
        return {
            "chrome": [
                rf"{pf}\\Google\\Chrome\\Application\\chrome.exe",
                rf"{pf86}\\Google\\Chrome\\Application\\chrome.exe",
                rf"{lad}\\Google\\Chrome\\Application\\chrome.exe",
            ],
            "quark": [
                rf"{pf}\\Quark\\Application\\quark.exe",
                rf"{pf86}\\Quark\\Application\\quark.exe",
                rf"{lad}\\Quark\\Application\\quark.exe",
            ],
        }
    return {"chrome": [], "quark": []}


def _apply_overrides(paths: dict[str, list[str]]) -> dict[str, list[str]]:
    overrides = os.environ.get("BROWSER_PATH_OVERRIDES")
    if not overrides:
        return paths
    try:
        data = json.loads(overrides)
    except json.JSONDecodeError:
        return paths
    if not isinstance(data, dict):
        return paths
    for key, value in data.items():
        if isinstance(value, list):
            paths[key] = value
    return paths


def _exists(path_str: str) -> bool:
    return Path(path_str).exists()


def _find_installed(paths: dict[str, list[str]]) -> dict[str, list[str]]:
    installed: dict[str, list[str]] = {"chrome": [], "quark": []}
    for name, candidates in paths.items():
        for raw in _expand_paths(candidates):
            if _exists(raw):
                installed[name].append(raw)
    return installed


def _select_browser(installed: dict[str, list[str]]) -> str | None:
    for name in ("chrome", "quark"):
        if installed.get(name):
            return name
    return None


def _install_command(os_name: str) -> str | None:
    if os_name == "macos":
        return "brew install --cask google-chrome"
    if os_name == "windows":
        return "winget install --id Google.Chrome -e"
    return None


def _open_command(os_name: str, browser: str, url: str) -> str:
    if os_name == "macos":
        app_name = {
            "chrome": "Google Chrome",
            "quark": "Quark",
        }.get(browser, browser)
        return f"open -a \"{app_name}\" '{url}'"
    if os_name == "windows":
        exe = {
            "chrome": "chrome.exe",
            "quark": "quark.exe",
        }.get(browser, "chrome.exe")
        return f"start \"\" {exe} {url}"
    return ""


def _close_command(os_name: str, browser: str) -> str:
    if os_name == "macos":
        app_name = {
            "chrome": "Google Chrome",
            "quark": "Quark",
        }.get(browser, browser)
        return f"osascript -e 'quit app \"{app_name}\"'"
    if os_name == "windows":
        exe = {
            "chrome": "chrome.exe",
            "quark": "quark.exe",
        }.get(browser, "chrome.exe")
        return f"taskkill /IM {exe} /F"
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--url", default="https://www.google.com")
    args = parser.parse_args()

    os_name = "macos" if _is_macos() else "windows" if _is_windows() else "other"

    paths = _apply_overrides(_default_browser_paths())
    installed = _find_installed(paths)
    browser = _select_browser(installed)

    plan = {
        "os": os_name,
        "installed": installed,
        "selected_browser": browser,
        "install_chrome": None,
        "open_command": None,
        "close_command": None,
    }

    if browser:
        plan["open_command"] = _open_command(os_name, browser, args.url)
        plan["close_command"] = _close_command(os_name, browser)
    else:
        plan["install_chrome"] = _install_command(os_name)

    if args.json:
        print(json.dumps(plan, indent=2, ensure_ascii=False))
        return 0

    print(f"OS: {os_name}")
    print(f"Selected browser: {browser}")
    if browser:
        print(f"Open command: {plan['open_command']}")
        print(f"Close command: {plan['close_command']}")
    else:
        print("No supported browsers found.")
        if plan["install_chrome"]:
            print(f"Install Chrome: {plan['install_chrome']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
