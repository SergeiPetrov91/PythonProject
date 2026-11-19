from playwright.sync_api import Page, expect


def test_loc(page: Page) -> None:
    page.goto("https://zimaev.github.io/text_input/")

    # Используем разные встроенные локаторы для каждого поля формы
    page.get_by_label("Email address").fill("qa@example.com")
    page.get_by_title("username").fill("Anton")
    page.get_by_placeholder("password").fill("secret")
    page.get_by_role("checkbox").click()

    # Проверяем, что значения заполнились и чекбокс отмечен
    expect(page.get_by_label("Email address")).to_have_value("qa@example.com")
    expect(page.get_by_role("checkbox")).to_be_checked()

    # Нажимаем кнопку отправки формы по ее роли и тексту
    page.get_by_role("button", name="Submit").click()
