import asyncio
import os
from playwright.async_api import async_playwright

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_URL = f"file:///{os.path.join(BASE_DIR, 'index.html').replace(os.sep, '/')}"
OUTPUT_DIR = os.path.join(BASE_DIR, "tools", "verified_screenshots")
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def capture():
    async with async_playwright() as p:
        # 1. DESKTOP CAPTURE (1400x800)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1400, "height": 800})
        
        print("Loading app on Desktop...")
        await page.goto(INDEX_URL)
        await page.wait_for_timeout(1000)
        
        # Enter application
        enter_btn = page.locator("#btn-enter-gateway")
        if await enter_btn.is_visible():
            await enter_btn.click()
            await page.wait_for_timeout(600)

        # Ensure Devanagari mode
        await page.evaluate("""() => {
            const btn = document.querySelector('.view-btn[data-view=\"devanagari\"]');
            if (btn) btn.click();
        }""")
        await page.wait_for_timeout(400)

        # 1. Chapter 1 Slide 1
        await page.evaluate("() => window.app.loadChapter(1)")
        await page.wait_for_timeout(500)
        p1 = os.path.join(OUTPUT_DIR, "desktop_ch1_s1.png")
        await page.screenshot(path=p1)
        print("Saved:", p1)

        # 2. Chapter 1 Slide 2
        await page.evaluate("() => window.app.renderSlide(1)")
        await page.wait_for_timeout(500)
        p2 = os.path.join(OUTPUT_DIR, "desktop_ch1_s2.png")
        await page.screenshot(path=p2)
        print("Saved:", p2)

        # 3. Chapter 1 Slide 6 (Shiva-Parvati Bronze Statue)
        await page.evaluate("() => window.app.renderSlide(5)")
        await page.wait_for_timeout(500)
        p3 = os.path.join(OUTPUT_DIR, "desktop_ch1_s6.png")
        await page.screenshot(path=p3)
        print("Saved:", p3)

        # 4. Chapter 2 Slide 1 (Buddha Head + Alphabet)
        await page.evaluate("() => window.app.loadChapter(2)")
        await page.wait_for_timeout(500)
        p4 = os.path.join(OUTPUT_DIR, "desktop_ch2_s1.png")
        await page.screenshot(path=p4)
        print("Saved:", p4)

        # 5. Chapter 3 Slide 1 (Kalidasa + Chitrakavya)
        await page.evaluate("() => window.app.loadChapter(3)")
        await page.wait_for_timeout(500)
        p5 = os.path.join(OUTPUT_DIR, "desktop_ch3_s1.png")
        await page.screenshot(path=p5)
        print("Saved:", p5)

        await page.close()

        # 2. MOBILE CAPTURE (375x667 - iPhone SE / Standard Mobile)
        mobile_page = await browser.new_page(viewport={"width": 375, "height": 667})
        await mobile_page.goto(INDEX_URL)
        await mobile_page.wait_for_timeout(1000)
        enter_m = mobile_page.locator("#btn-enter-gateway")
        if await enter_m.is_visible():
            await enter_m.click()
            await mobile_page.wait_for_timeout(600)

        # Chapter 1 Slide 6 on Mobile (Two-Tier Stack)
        await mobile_page.evaluate("() => { window.app.loadChapter(1); window.app.renderSlide(5); }")
        await mobile_page.wait_for_timeout(500)
        pm1 = os.path.join(OUTPUT_DIR, "mobile_ch1_s6.png")
        await mobile_page.screenshot(path=pm1)
        print("Saved:", pm1)

        # Chapter 2 Slide 1 on Mobile
        await mobile_page.evaluate("() => { window.app.loadChapter(2); }")
        await mobile_page.wait_for_timeout(500)
        pm2 = os.path.join(OUTPUT_DIR, "mobile_ch2_s1.png")
        await mobile_page.screenshot(path=pm2)
        print("Saved:", pm2)

        # Chapter 3 Slide 1 on Mobile (Dual-Pane stacked)
        await mobile_page.evaluate("() => { window.app.loadChapter(3); }")
        await mobile_page.wait_for_timeout(500)
        pm3 = os.path.join(OUTPUT_DIR, "mobile_ch3_s1.png")
        await mobile_page.screenshot(path=pm3)
        print("Saved:", pm3)

        await browser.close()
        print("All desktop and mobile verification screenshots captured successfully!")

if __name__ == "__main__":
    asyncio.run(capture())
