from playwright.sync_api import Page, expect


def test_drag_and_drop(page: Page) -> None:
    page.goto("https://zimaev.github.io/draganddrop/", wait_until="domcontentloaded")

    # Перетаскиваем элемент #drag в область #drop
    page.drag_and_drop("#drag", "#drop")

    # Проверяем, что элемент #drag теперь находится внутри блока #drop
    expect(page.locator("#drop #drag")).to_be_visible()
