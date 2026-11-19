import os
from playwright.sync_api import Page


# Вариант 1: По реальному стенду demoqa.com
def test_download_demoqa(page: Page) -> None:
    page.goto("https://demoqa.com/upload-download", wait_until="domcontentloaded")

    with page.expect_download() as download_info:
        # Обращаемся к кнопке по её уникальному id (или через get_by_role("button", name="Download"))
        page.locator("#downloadButton").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./data/"
    full_path = os.path.join(destination_folder_path, file_name)

    download.save_as(full_path)

    assert os.path.exists(full_path)
    print(f"\nФайл с demoqa успешно скачан: {full_path}")


# Вариант 2: Локальный тест
def test_download_local(page: Page) -> None:
    page.set_content('<a href="data:text/plain;charset=utf-8,Hello%20Download" download="sample.txt">Download</a>')

    with page.expect_download() as download_info:
        page.locator('a:has-text("Download")').click()

    download = download_info.value
    full_path = os.path.join("./data/", download.suggested_filename)
    download.save_as(full_path)

    assert os.path.exists(full_path)

