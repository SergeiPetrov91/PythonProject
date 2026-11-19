from playwright.sync_api import Page

def test_mock_tags(page):
    page.route("**/api/tags", lambda route: route.fulfill(path="data.json"))
    page.goto('https://demo.realworld.io/')
    