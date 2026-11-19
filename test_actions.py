from playwright.sync_api import Page, expect

def test_fill_method(page: Page) -> None:
        page.goto("https://zimaev.github.io/text_input/", wait_until="domcontentloaded")
        email_input = page.get_by_label("Email address")
        email_input.fill("admin@example.com")
        expect(email_input).to_have_value("admin@example.com")

def test_press_sequentially_method(page: Page) -> None:
        page.goto("https://zimaev.github.io/text_input/", wait_until="domcontentloaded")
        username_input = page.get_by_title("username")
        username_input.press_sequentially("Anton", delay=100)
        expect(username_input).to_have_value("Anton")

def test_press_key_method(page: Page) -> None:
        page.goto("https://zimaev.github.io/text_input/", wait_until="domcontentloaded")
        password_input = page.get_by_placeholder("password")
        password_input.fill("secret123")
        password_input.press("Tab")
        expect(password_input).to_have_value("secret123")

def test_click_method(page: Page) -> None:
        page.goto("https://zimaev.github.io/text_input/", wait_until="domcontentloaded")
        checkbox = page.get_by_role("checkbox")
        checkbox.click()
        expect(checkbox).to_be_checked()


def test_input_and_clicks(page: Page) -> None:
    page.goto("https://zimaev.github.io/text_input/", wait_until="domcontentloaded")

    # 1. Мгновенная вставка текста через fill()
    email_input = page.get_by_label("Email address")
    email_input.fill("admin@example.com")

    # 2. Посимвольный ввод с задержкой 100 мс (имитация живого набора)
    username_input = page.get_by_title("username")
    username_input.press_sequentially("Anton", delay=100)

    # 3. Заполнение пароля и нажатие Tab для перехода к следующему элементу
    password_input = page.get_by_placeholder("password")
    password_input.fill("secret123")
    password_input.press("Tab")

    # 4. Обычный клик по чекбоксу и отправка формы
    page.get_by_role("checkbox").click()
    expect(email_input).to_have_value("admin@example.com")
    expect(username_input).to_have_value("Anton")
