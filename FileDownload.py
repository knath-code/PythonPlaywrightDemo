import asyncio
from playwright.async_api import async_playwright


def download_handal(download):
    location_file = './Flies/test.zip'
    download.save_as(location_file)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://demo.imacros.net/Automate/Downloads")
        page.on('download', download_handal)
        download_button = await page.wait_for_selector('//a[@href="/Content/Download.zip"]')
        await download_button.click()
        await page.wait_for_timeout(5000)
        await browser.close()

asyncio.run(main())