from playwright.sync_api import Page, Route, expect


# Вариант 1: Полная подмена ответа от сервера без отправки реального запроса
def test_mock_response(page: Page) -> None:
    page.route(
        "**/api/tags",
        lambda route: route.fulfill(
            json={"tags": ["playwright", "python", "qa"]}
        ),
    )

    page.goto("https://conduit.bondaracademy.com/")
    sidebar = page.locator("div.sidebar")
    expect(sidebar.locator(".tag-pill")).to_contain_text(["playwright", "python", "qa"])


# Вариант 2: Перехват реального ответа, изменение данных и отправка в браузер
def test_intercepted(page: Page) -> None:
    def handle_route(route: Route) -> None:
        response = route.fetch()
        json_data = response.json()
        json_data["tags"] = ["open", "solutions"]
        route.fulfill(json=json_data)

    page.route("**/api/tags", handle_route)

    page.goto("https://conduit.bondaracademy.com/")
    sidebar = page.locator("div.sidebar")
    expect(sidebar.locator(".tag-pill")).to_contain_text(["open", "solutions"])
