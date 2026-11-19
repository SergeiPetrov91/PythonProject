from playwright.sync_api import Page, expect

def test_navbar_chain(page: Page) -> None:
        page.goto("https://zimaev.github.io/navbar/", wait_until="domcontentloaded")
        nav_bar = page.locator("div#navbarNavDropdown")
        nav_bar.locator("li").filter(has_text="Company").click()
        expect(page.get_by_text("About Us")).to_be_visible()

def test_table_filter(page: Page) -> None:
        page.goto("https://zimaev.github.io/filter/", wait_until="domcontentloaded")
        row_locator = page.locator("tr")

        rows_without_button = row_locator.filter(has_not=page.get_by_role("button")).count()
        rows_without_helicopter = row_locator.filter(has_not_text="helicopter").count()
        print(f"\nСтрок без кнопок: {rows_without_button}")
        print(f"Строк без 'helicopter': {rows_without_helicopter}")

        # Находим строку со словом "helicopter" и нажимаем на кнопку внутри неё
        target_row = row_locator.filter(has_text="helicopter")
        target_row.get_by_role("button").click()

