import asyncio
from playwright.async_api import async_playwright
import tracemalloc
tracemalloc.start()

alert_text = []


def handel_dialog(dialog):
    message = dialog.message
    alert_text.append(message)
    dialog.dismiss()


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://demo.automationtesting.in/Alerts.html")
        # await page.wait_for_selector('//div[@id="OKTab"]/button')

        alert_with_ok = await page.wait_for_selector('//a[@href="#CancelTab"]')
        await alert_with_ok.click()
        await page.wait_for_timeout(2000)
        page.on("dialog", handel_dialog)
        confirm_box = await page.wait_for_selector('//div[@id="CancelTab"]/button')
        await confirm_box.click()
        await page.wait_for_timeout(3000)
        print(alert_text[0])
        await browser.close()



asyncio.run(main())