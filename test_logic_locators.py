from playwright.sync_api import Page, expect


def test_locator_and(page: Page) -> None:
    page.goto("https://zimaev.github.io/locatorand/")

    # Находим строго кнопку "Sing up", у которой атрибут title равен "Sing up today"
    target_button = page.get_by_role("button", name="Sing up").and_(
        page.get_by_title("Sing up today")
    )

    expect(target_button).to_be_visible()
    target_button.click()
