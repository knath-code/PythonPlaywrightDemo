import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://demo.automationtesting.in/Selectable.html")
        # Hover the dropdown
        hover_dropdown = await page.wait_for_selector('//a[text()="SwitchTo"]')
        await hover_dropdown.hover()
        # Click on element
        element_click = await page.wait_for_selector('//a[text()="SwitchTo"]')
        await element_click.click()
        # Double Click
        double_click = await page.wait_for_selector('//a[text()="SwitchTo"]')
        await double_click.dblclick()
        #  Right on Element
        right_element = await page.wait_for_selector('//a[text()="SwitchTo"]')
        await right_element.click(button="right")
        # shift click
        shift_click = await page.wait_for_selector('//a[text()="SwitchTo"]')
        await shift_click.click(modifiers=["Shift"])
        # Keyboard
        keyboard = await page.wait_for_selector('//a[text()="SwitchTo"]')
        await keyboard.press("A")
        # Backquote, Minus, Equal, Backslash, Backspace, Tab, Delete, Escape,
        # ArrowDown, End, Enter, Home, Insert, PageDown, PageUp, ArrowRight,
        # ArrowUp, F1 - F12, Digit0 - Digit9, KeyA - KeyZ, etc.
        keyboard_all = await  page.wait_for_selector('//a[text()="SwitchTo"]')
        await keyboard_all.press("$")

        await page.wait_for_timeout(3000)
        await browser.close()

asyncio.run(main())