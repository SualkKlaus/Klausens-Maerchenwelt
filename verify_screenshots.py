#!/usr/bin/env python3
"""Lokale Screenshots der statischen Maerchenseite erstellen."""

from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent


def shot(page, name, width, height):
    page.set_viewport_size({"width": width, "height": height})
    page.goto((ROOT / name).as_uri(), wait_until="networkidle")
    page.screenshot(path=str(ROOT / f"verify-{name}-{width}.png"), full_page=True)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        shot(page, "index.html", 1366, 900)
        shot(page, "index.html", 390, 844)
        shot(page, "geschichte-1.html", 900, 900)
        shot(page, "geschichte-8.html", 900, 900)
        browser.close()


if __name__ == "__main__":
    main()
