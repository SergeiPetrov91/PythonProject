# from playwright.sync_api import Page
#
#
# def test_get_table_values(page: Page) -> None:
#     page.goto("https://zimaev.github.io/table/", wait_until="domcontentloaded")
#     rows = page.locator("tr")
#
#     # 1. Получаем списки текста всех строк таблицы двумя способами
#     print("\n--- all_inner_texts() ---")
#     print(rows.all_inner_texts())
#
#     print("\n--- all_text_contents() ---")
#     print(rows.all_text_contents())
#
#     # 2. Получаем текст и HTML-разметку первой строки с данными (индекс 1, так как 0 — шапка таблицы)
#     first_user_row = rows.nth(1)
#     print("\n--- inner_text() одной строки ---")
#     print(first_user_row.inner_text())
#
#     print("\n--- inner_html() одной строки ---")
#     print(first_user_row.inner_html())
#
#     # Проверяем, что в таблице есть ожидаемый пользователь
#     assert "Mark" in first_user_row.inner_text()

from playwright.sync_api import Page


def test_get_table_values(page: Page) -> None:
    page.goto("https://zimaev.github.io/table/", wait_until="domcontentloaded")
    rows = page.locator("tr")

    print("\n--- all_inner_texts() ---")
    print(rows.all_inner_texts())

    print("\n--- all_text_contents() ---")
    print(rows.all_text_contents())

    first_user_row = rows.nth(1)
    print("\n--- inner_text() одной строки ---")
    print(first_user_row.inner_text())

    print("\n--- inner_html() одной строки ---")
    print(first_user_row.inner_html())

    # Пауза 5 секунд, чтобы рассмотреть таблицу в браузере
    page.wait_for_timeout(5000)

    assert "Mark" in first_user_row.inner_text()
