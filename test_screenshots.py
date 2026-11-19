import os
from playwright.sync_api import Page


def test_take_screenshots(page: Page) -> None:
    page.goto("https://zimaev.github.io/tabs/", wait_until="domcontentloaded")

    # 1. Скриншот всей страницы (PNG)
    page.screenshot(path="screenshots/full_page.png", full_page=True)

    # 2. Скриншот отдельного элемента на текущей странице
    page.get_by_text("Переход к Dashboard").screenshot(path="screenshots/element_only.png")

    # 3. Скриншот в формате JPEG со сжатием качества 80%
    page.screenshot(path="screenshots/compressed.jpeg", type="jpeg", quality=80)

    assert os.path.exists("screenshots/full_page.png")
    assert os.path.exists("screenshots/element_only.png")
    assert os.path.exists("screenshots/compressed.jpeg")

