from playwright.sync_api import Page, expect


# 1. Нажимаем "OK" в окне Confirmation и проверяем появление текста на странице
def test_dialog_confirm_accept(page: Page) -> None:
    page.goto("https://zimaev.github.io/dialog/", wait_until="domcontentloaded")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Диалог Confirmation").click()
    expect(page.get_by_text("Изменения сохранены!")).to_be_visible()


# 2. Нажимаем "Отмена" в окне Confirmation
def test_dialog_confirm_dismiss(page: Page) -> None:
    page.goto("https://zimaev.github.io/dialog/", wait_until="domcontentloaded")
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.get_by_text("Диалог Confirmation").click()
    expect(page.get_by_text("Изменения не сохранены!")).to_be_visible()


# 3. Вводим текст в окно Prompt и нажимаем "OK"
def test_dialog_prompt(page: Page) -> None:
    page.goto("https://zimaev.github.io/dialog/", wait_until="domcontentloaded")
    page.on("dialog", lambda dialog: dialog.accept("Привет, Playwright!"))
    page.get_by_text("Диалог Prompt").click()
