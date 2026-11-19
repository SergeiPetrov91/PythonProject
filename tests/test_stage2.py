import os
from playwright.sync_api import Page, expect


# --- 1. КНОПКИ И ПЕРЕКЛЮЧАТЕЛИ ---
def test_buttons_positive_and_negative(page: Page) -> None:
    page.goto("https://demoqa.com" + "/buttons", wait_until="domcontentloaded")

    page.locator("#doubleClickBtn").dblclick()
    expect(page.locator("#doubleClickMessage")).to_have_text("You have done a double click")

    page.locator("#rightClickBtn").click(button="right")
    expect(page.locator("#rightClickMessage")).to_have_text("You have done a right click")

    page.get_by_role("button", name="Click Me", exact=True).click()
    expect(page.locator("#dynamicClickMessage")).to_have_text("You have done a dynamic click")

    page.goto("https://demoqa.com" + "/radio-button", wait_until="domcontentloaded")
    expect(page.locator("#noRadio")).to_be_disabled()


# --- 2. ВСПЛЫВАЮЩИЕ ОКНА И АЛЕРТЫ ---
def test_popups_accept_and_dismiss(page: Page) -> None:
    page.goto("https://practice-automation.com" + "/popups/", wait_until="domcontentloaded")

    page.once("dialog", lambda dialog: dialog.accept())
    page.locator("#confirm").click()
    expect(page.locator("#confirmResult")).to_have_text("OK it is!")

    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator("#confirm").click()
    expect(page.locator("#confirmResult")).to_have_text("Cancel it is!")

    page.once("dialog", lambda dialog: dialog.accept("Playwright"))
    page.locator("#prompt").click()
    expect(page.locator("#promptResult")).to_have_text("Nice to meet you, Playwright!")


# --- 3. ЗАГРУЗКА ФАЙЛОВ ---
def test_file_upload_positive_and_negative(page: Page) -> None:
    page.goto("https://practice-automation.com" + "/file-upload/", wait_until="domcontentloaded")

    # Позитивный сценарий: загрузка разрешенного .txt файла
    with open("valid_test.txt", "w") as f:
        f.write("Valid content")

    page.locator("#file-upload").set_input_files("valid_test.txt")
    page.locator("#upload-btn").click()
    expect(page.locator(".wpcf7-response-output")).to_contain_text(
        "Thank you for your message. It has been sent.", timeout=10000
    )

    # Негативный сценарий: попытка загрузить запрещенный формат (.exe)
    page.reload(wait_until="domcontentloaded")
    with open("invalid_test.exe", "w") as f:
        f.write("Fake exe")

    page.locator("#file-upload").set_input_files("invalid_test.exe")
    page.locator("#upload-btn").click()
    # Обращаемся строго к элементу ошибки под полем ввода
    expect(page.locator(".wpcf7-not-valid-tip")).to_contain_text(
        "You are not allowed to upload files of this type", timeout=10000
    )

    # Удаляем временные файлы
    os.remove("valid_test.txt")
    os.remove("invalid_test.exe")


