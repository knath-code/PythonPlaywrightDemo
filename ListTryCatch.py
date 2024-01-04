import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto("https://demo.automationtesting.in/Selectable.html")

            # store multiple element on the list
            elements = await page.query_selector_all('b')
            print(len(elements))
            for i in elements:
                print(await i.text_content())

            # store multiple links on this list
            elements = await page.query_selector_all('a')
            print(len(elements))
            for i in elements:
                print(await i.get_attribute('href'))

            # To check try catch with wrong xpath
            trycatch = await page.query_selector('d//[@sf="werf"]')
            await trycatch.click()

            await page.wait_for_timeout(3000)
            await browser.close()
        except Exception as e:
            print(str(e))
        finally:
            print("Successfuly code execute")
asyncio.run(main())