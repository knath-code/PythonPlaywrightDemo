import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://google.com")
        print(await page.title())
        print("Chrome successfully opened ")
        await page.wait_for_timeout(3000)
        await browser.close()

asyncio.run(main())