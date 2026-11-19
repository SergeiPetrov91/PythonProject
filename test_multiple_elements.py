from playwright.sync_api import Page, expect


def test_check_all_inputs(page: Page) -> None:
    page.goto("https://zimaev.github.io/checks-radios/", wait_until="domcontentloaded")

    # Находим все элементы input (чекбоксы, радиокнопки и переключатели)
    checkboxes = page.locator("input")

    # Проходим по каждому элементу с помощью современного метода .all()
    for checkbox in checkboxes.all():
        checkbox.check()
        expect(checkbox).to_be_checked()
