import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://demo.automationtesting.in/Windows.html")
        text_button = await page.wait_for_selector('//button[contains(text()," click ")]')
        await text_button.click()
        await page.wait_for_timeout(3000)
        total_pages = context.pages
        print(len(total_pages))
        for i in total_pages:
            print(i)
        print(await page.title())
        new_page = total_pages[1]
        await new_page.bring_to_front()
        await page.wait_for_timeout(3000)
        print(new_page.title())
        await new_page.close()
        await page.wait_for_timeout(5000)
        await browser.close()

asyncio.run(main())