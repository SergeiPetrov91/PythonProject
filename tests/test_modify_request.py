from playwright.sync_api import Page


def test_modify_request(page: Page) -> None:
    page.route(
        "**/api/register",
        lambda route: route.continue_(
            post_data='{"email": "user", "password": "secret"}'
        ),
    )

    page.goto("https://reqres.in")

    with page.expect_response("**/api/register") as response_info:
        page.evaluate(
            """fetch('/api/register', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({email: 'eve.holt@reqres.in', password: 'pistol'})
            })"""
        )

    response = response_info.value
    assert response.status == 400
