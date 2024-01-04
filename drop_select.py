import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://demo.automationtesting.in/Register.html")
        # Find  the select location
        # select_dropdown = await page.query_selector('//select[@id ="Skills"]')
        # Select the option
        # await select_dropdown.select_option(label='AutoCAD')

        await page.select_option('//select[@id ="Skills"]',label='Analytics')
        await page.wait_for_timeout(5000)
        await browser.close()

asyncio.run(main())








