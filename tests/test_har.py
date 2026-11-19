from playwright.sync_api import Page, expect

def test_har_py(page: Page) -> None:
    page.route_from_har("example.har", not_found="fallback")

    page.goto("https://reqres.in/")
    page.get_by_role("button", name="Send request").click()
    expect(page.locator("body")).to_contain_text("Open Solutions")

