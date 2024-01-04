import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://demo.automationtesting.in/Register.html")
        # To select radio button
        radio_button = await page.query_selector('//input[@value ="Male"]')
        # click radio button
        await radio_button.check()
        await asyncio.sleep(1)
        if await radio_button.is_checked():
            print("radio button check successfully")
        else:
            print("Failed")

        checkbox = await page.query_selector('//input[@value ="Movies"]')
        await checkbox.click()

        if await checkbox.is_checked():
            print("checkbox click successfully")
        else:
            print("Failed")

        await page.wait_for_timeout(5000)
        await browser.close()


asyncio.run(main())