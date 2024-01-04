import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://demo.automationtesting.in/FileUpload.html")
        file_upload = './kam.txt'
        upload_location = await page.query_selector('//input[@id ="input-4"]')
        # To upload file
        await upload_location.set_input_files(file_upload)
        await page.wait_for_timeout(3000)
        await browser.close()

asyncio.run(main())