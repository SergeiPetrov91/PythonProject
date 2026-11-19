from playwright.sync_api import Page, expect


# 1. Позитивный + негативный тест на чекбоксы (the-internet)
def test_checkboxes_the_internet(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/checkboxes", wait_until="domcontentloaded")
    checkboxes = page.locator("input[type='checkbox']")

    # Первый чекбокс изначально выключен -> включаем
    expect(checkboxes.nth(0)).not_to_be_checked()
    checkboxes.nth(0).check()
    expect(checkboxes.nth(0)).to_be_checked()

    # Второй чекбокс изначально включен -> выключаем
    expect(checkboxes.nth(1)).to_be_checked()
    checkboxes.nth(1).uncheck()
    expect(checkboxes.nth(1)).not_to_be_checked()


# 2. Позитивный + негативный тест на выпадающий список (the-internet)
def test_dropdown_the_internet(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dropdown", wait_until="domcontentloaded")
    dropdown = page.locator("#dropdown")

    # Негативная проверка: пункт по умолчанию "Please select an option" заблокирован
    expect(dropdown.locator("option").first).to_be_disabled()

    # Позитивная проверка: выбираем Option 1 и Option 2
    dropdown.select_option("1")
    expect(dropdown).to_have_value("1")

    dropdown.select_option(label="Option 2")
    expect(dropdown).to_have_value("2")


# 3. Позитивный + негативный тест на Selected & Disabled (webdriveruniversity)
def test_disabled_controls_webdriveruniv(page: Page) -> None:
    page.goto(
        "https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html",
        wait_until="domcontentloaded",
    )

    # Негативная проверка: радиокнопка Cabbage и опция Orange в списке недоступны для выбора
    expect(page.locator("input[value='cabbage']")).to_be_disabled()
    expect(page.locator("#fruit-selects option[value='orange']")).to_be_disabled()

    # Позитивная проверка: радиокнопка Pumpkin активна и выбрана по умолчанию, переключаем на Lettuce
    expect(page.locator("input[value='pumpkin']")).to_be_checked()
    page.locator("input[value='lettuce']").check()
    expect(page.locator("input[value='lettuce']")).to_be_checked()
    expect(page.locator("input[value='pumpkin']")).not_to_be_checked()
