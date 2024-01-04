import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://www.redbus.in")
        # checking cookies
        my_cookies = await page.context.cookies()
        print(my_cookies)
        # Clearing all the cookies.
        await page.context.clear_cookies()
        # Setting new cookies to page.

        new_cookies = {
            'name': 'kam',
            'udid': '313242dw42323' }

        # pass new cookies
        # await page.context.add_cookies([new_cookies])

        await page.screenshot(path='test.png', full_page=True)

        await page.wait_for_timeout(1000)
        await browser.close()

asyncio.run(main())