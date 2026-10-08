import asyncio
import os
import sys
from playwright.async_api import async_playwright

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_URL = f"file:///{os.path.join(BASE_DIR, 'index.html').replace(os.sep, '/')}"
OUTPUT_DIR = os.path.join(BASE_DIR, "tools", "verified_screenshots")
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1400, "height": 800})
        page = await context.new_page()

        print(f"Loading {INDEX_URL}...")
        await page.goto(INDEX_URL)
        await page.wait_for_timeout(1000)

        # Enter curriculum directly
        enter_btn = page.locator("#btn-enter-gateway")
        if await enter_btn.is_visible():
            await enter_btn.click()
            await page.wait_for_timeout(600)

        # Ensure Devanagari mode is active
        await page.evaluate("""() => {
            const btn = document.querySelector('.view-btn[data-view=\"devanagari\"]');
            if (btn) btn.click();
        }""")
        await page.wait_for_timeout(400)

        # Capture Chapter 1 Slide 1
        pic1_path = os.path.join(OUTPUT_DIR, "verified_pic1_ch1.png")
        await page.screenshot(path=pic1_path)
        print(f"Saved: {pic1_path}")

        # Navigate to Chapter 2
        await page.evaluate("() => window.DevabhashaInstance.loadChapter(2)")
        await page.wait_for_timeout(600)
        pic2_path = os.path.join(OUTPUT_DIR, "verified_pic2_ch2.png")
        await page.screenshot(path=pic2_path)
        print(f"Saved: {pic2_path}")

        # Navigate to Chapter 3
        await page.evaluate("() => window.DevabhashaInstance.loadChapter(3)")
        await page.wait_for_timeout(600)
        pic3_path = os.path.join(OUTPUT_DIR, "verified_pic3_ch3.png")
        await page.screenshot(path=pic3_path)
        print(f"Saved: {pic3_path}")

        # Navigate to Chapter 4
        await page.evaluate("() => window.DevabhashaInstance.loadChapter(4)")
        await page.wait_for_timeout(600)
        pic4_path = os.path.join(OUTPUT_DIR, "verified_pic4_ch4.png")
        await page.screenshot(path=pic4_path)
        print(f"Saved: {pic4_path}")

        # Navigate to Chapter 5
        await page.evaluate("() => window.DevabhashaInstance.loadChapter(5)")
        await page.wait_for_timeout(600)
        pic5_path = os.path.join(OUTPUT_DIR, "verified_pic5_ch5.png")
        await page.screenshot(path=pic5_path)
        print(f"Saved: {pic5_path}")

        await browser.close()
        print("All 5 verification screenshots captured successfully!")

if __name__ == "__main__":
    asyncio.run(capture())
