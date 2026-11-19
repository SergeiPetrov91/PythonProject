from playwright.sync_api import Page, expect


# Вариант 1: через .check() — все чекбоксы гарантированно останутся отмеченными
def test_checkbox_with_check(page: Page) -> None:
    page.goto("https://zimaev.github.io/checks-radios/", wait_until="domcontentloaded")
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()

    expect(page.locator("text=Default checkbox")).to_be_checked()
    expect(page.locator("text=Checked checkbox")).to_be_checked()
    expect(page.locator("text=Checked switch checkbox input")).to_be_checked()


# Вариант 2: через .click() — уже отмеченные элементы переключатся в выключенное состояние
def test_checkbox_with_click(page: Page) -> None:
    page.goto("https://zimaev.github.io/checks-radios/", wait_until="domcontentloaded")
    page.locator("text=Default checkbox").click()
    page.locator("text=Checked checkbox").click()
    page.locator("text=Default radio").click()
    page.locator("text=Default checked radio").click()
    page.locator("text=Checked switch checkbox input").click()

    expect(page.locator("text=Default checkbox")).to_be_checked()
    expect(page.locator("text=Checked checkbox")).not_to_be_checked()
    expect(page.locator("text=Checked switch checkbox input")).not_to_be_checked()

