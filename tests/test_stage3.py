import re
from playwright.sync_api import Page, expect


# --- 1. ДИНАМИЧЕСКАЯ ТАБЛИЦА ---
def test_dynamic_table_cpu(page: Page) -> None:
    page.goto("http://uitestingplayground" + ".com/dynamictable", wait_until="domcontentloaded")

    headers = page.locator("[role='columnheader']").all_inner_texts()
    cpu_col_index = headers.index("CPU")

    chrome_row = page.locator("[role='row']").filter(has_text="Chrome")
    cpu_value = chrome_row.locator("[role='cell']").nth(cpu_col_index).inner_text()

    expect(page.locator(".bg-warning")).to_have_text(f"Chrome CPU: {cpu_value}")


# --- 2. АВТОРИЗАЦИЯ: НЕГАТИВНЫЙ И ПОЗИТИВНЫЙ СЦЕНАРИИ ---
def test_login_negative_and_positive(page: Page) -> None:
    page.goto("https://the-internet." + "herokuapp.com/login", wait_until="domcontentloaded")

    # Негативный сценарий: неверный пароль
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("WrongPassword123")
    page.locator("button[type='submit']").click()
    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")

    # Позитивный сценарий: правильные логин и пароль
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")


# --- 3. ПОЛНЫЙ E2E-СЦЕНАРИЙ ИНТЕРНЕТ-МАГАЗИНА SAUCEDEMO ---
def test_saucedemo_e2e_purchase(page: Page) -> None:
    page.goto("https://www." + "saucedemo.com/", wait_until="domcontentloaded")

    # Негативная проверка: заблокированный пользователь
    page.locator("[data-test='username']").fill("locked_out_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    expect(page.locator("[data-test='error']")).to_contain_text("Sorry, this user has been locked out.")

    # Позитивная авторизация под стандартным пользователем
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))

    # Добавляем рюкзак в корзину и переходим к оформлению
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    page.locator(".shopping_cart_link").click()
    page.locator("[data-test='checkout']").click()

    # Заполняем данные покупателя и завершаем заказ
    page.locator("[data-test='firstName']").fill("Sergei")
    page.locator("[data-test='lastName']").fill("Petrov")
    page.locator("[data-test='postalCode']").fill("190000")
    page.locator("[data-test='continue']").click()

    page.locator("[data-test='finish']").click()
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
