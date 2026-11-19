# project/pages/login_page.py
from typing import Any

from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page


class LoginPage(Page):
    def __init__(self, page : Page):
        self.page = page

        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.user_button = page.locator('#login')
        self.error_message = page.locator('#errorAlert')

    def navigate(self):
        self.page.goto('https://zimaev.github.io/pom/')

    def login(self, username : str, password : str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.user_button.click()

    def get_error_message(self):
        return self.error_message.inner_text()

