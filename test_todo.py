from playwright.sync_api import Page, expect


def test_add_todo(page: Page) -> None:
    page.goto("https://todomvc.com")
    page.get_by_role("link", name="React").first.click()

    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    expect(page.get_by_text("Создать первый сценарий playwright")).to_be_visible()








