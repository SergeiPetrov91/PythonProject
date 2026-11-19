from playwright.sync_api import Page, Response


def test_listen_network(page: Page) -> None:
    server_errors = []

    def handle_response(response: Response) -> None:
        print("<<", response.status, response.url)
        if response.status >= 500:
            server_errors.append((response.status, response.url))

    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", handle_response)

    page.goto("https://example.com/")

    assert len(server_errors) == 0, f"Найдены ошибки сервера: {server_errors}"



