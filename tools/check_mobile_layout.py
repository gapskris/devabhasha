import asyncio
from playwright.async_api import async_playwright

async def check_mobile():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 375, "height": 667})
        await page.goto("file:///C:/DataScience/Vijay%20Ji%27s%20Music%20Conversion/Devabhasha_modern/index.html")
        await page.wait_for_timeout(1000)
        await page.click("#btn-enter-gateway")
        await page.wait_for_timeout(500)
        await page.evaluate("() => { window.app.loadChapter(1); window.app.renderSlide(5); }")
        await page.wait_for_timeout(500)
        
        info = await page.evaluate('''() => {
            const canvasBg = document.querySelector('.stage-canvas-bg');
            const wrap = document.querySelector('.dialogues-wrapper');
            const card = document.querySelector('.dialogues-wrapper .dialogue-card:not([style*="display: none"])');
            return {
                canvasBg: canvasBg ? canvasBg.getBoundingClientRect() : null,
                wrap: wrap ? wrap.getBoundingClientRect() : null,
                card: card ? card.getBoundingClientRect() : null,
                bodyHeight: document.body.scrollHeight,
                windowHeight: window.innerHeight
            };
        }''')
        print("Mobile layout info:", info)
        
        # Now scroll down by 200px and take screenshot of the card
        await page.evaluate("window.scrollTo(0, 200)")
        await page.wait_for_timeout(300)
        await page.screenshot(path="Devabhasha_modern/tools/verified_screenshots/mobile_ch1_s6_scrolled.png")
        print("Saved scrolled screenshot.")
        await browser.close()

asyncio.run(check_mobile())
