import asyncio
from playwright.async_api import async_playwright


base_url = 'https://www.plus2net.com/php_tutorial/dd-ajax.php?'


async def handle_rejex(response):
    if 'https://www.plus2net.com/php_tutorial/dd-ajax.php?' in response.url:
        status = response.status
        data = response.text()
        print(f'status:{status},data:{data}')


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php")
        select = await page.wait_for_selector('//select[@id="s1"]')
        page.on('response', lambda response: handle_rejex(response))
        await select.select_option('2')
        await page.wait_for_timeout(3000)
        await browser.close()

asyncio.run(main())