from playwright.sync_api import Page, expect


def test_select(page: Page) -> None:
    page.goto("https://zimaev.github.io/select/", wait_until="domcontentloaded")
    select = page.locator("#floatingSelect")

    # 1. Выбор по атрибуту value ("У меня лапки")
    select.select_option(value="3")
    expect(select).to_have_value("3")

    # 2. Выбор по индексу (1 -> "Предложил новую функцию")
    select.select_option(index=1)
    expect(select).to_have_value("2")

    # 3. Выбор по видимому тексту ("Нашел и завел bug")
    select.select_option(label="Нашел и завел bug")
    expect(select).to_have_value("1")


def test_select_multiple(page: Page) -> None:
    page.goto("https://zimaev.github.io/select/", wait_until="domcontentloaded")
    skills_select = page.locator("#skills")

    # Множественный выбор нескольких пунктов сразу
    skills_select.select_option(value=["playwright", "python"])
    expect(skills_select).to_have_values(["playwright", "python"])
