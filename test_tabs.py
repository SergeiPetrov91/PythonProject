from playwright.sync_api import Page, expect


def test_new_tab(page: Page) -> None:
    page.goto("https://zimaev.github.io/tabs/", wait_until="domcontentloaded")

    # Перехватываем открытие новой вкладки после клика
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
    new_tab.wait_for_load_state("domcontentloaded")

    # Проверяем URL и видимость ссылки Sign out на новой вкладке
    expect(new_tab).to_have_url("https://zimaev.github.io/tabs/dashboard/index.html?")
    sign_out = new_tab.locator(".nav-link", has_text="Sign out")
    expect(sign_out).to_be_visible()

    # При необходимости можно вернуться на первую вкладку
    page.bring_to_front()
