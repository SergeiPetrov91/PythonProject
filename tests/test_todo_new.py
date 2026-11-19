from playwright.sync_api import Page, expect


def test_todo_pause_demo(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")

    input_field = page.get_by_placeholder("What needs to be done?")
    expect(input_field).to_be_empty()

    input_field.fill("Закончить курс по playwright")
    input_field.press("Enter")

    # Ищем элементы списка задач по тегу li внутри .todo-list
    todo_item = page.locator(".todo-list li")
    expect(todo_item).to_have_count(1)
    expect(todo_item).to_have_text("Закончить курс по playwright")

