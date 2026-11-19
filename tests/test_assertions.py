import re
from playwright.sync_api import Page, expect

HOST = "https://" + "zimaev." + "github.io/"


def test_page_and_table_assertions(page: Page) -> None:
    page.goto(HOST + "table/", wait_until="domcontentloaded")

    # 1. Проверка заголовка вкладки (title) и адреса (URL)
    expect(page, "Неверный заголовок страницы").to_have_title("Table demo")
    expect(page).to_have_url(re.compile(r".*/table/"))

    # 2. Проверка точного количества строк в таблице (1 шапка + 3 пользователя = 4)
    rows = page.locator("tr")
    expect(rows, "В таблице должно быть ровно 4 строки").to_have_count(4)

    # 3. Проверка CSS-класса у самой таблицы
    table = page.locator("table")
    expect(table).to_have_class(re.compile(r".*table.*"))


def test_input_focus_and_attributes(page: Page) -> None:
    page.goto(HOST + "text_input/", wait_until="domcontentloaded")

    email_input = page.get_by_label("Email address")

    # 4. Проверка HTML-атрибута type="email" и пустого значения по умолчанию
    expect(email_input).to_have_attribute("type", "email")
    expect(email_input).to_be_empty()

    # 5. Клик по полю и проверка, что элемент получил фокус (курсор внутри)
    email_input.click()
    expect(email_input, "Поле Email должно быть в фокусе после клика").to_be_focused()
