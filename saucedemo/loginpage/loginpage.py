from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.logo = page.locator(".login_logo")
        self.form_container = page.locator(".login-box")
        self.bot_image = page.locator(".bot_column")
        self.cred_section = page.locator(".login_credentials")
        self.password_section = page.locator(".login_password")

    def goto(self):
        self.page.goto("https://www.saucedemo.com/v1/index.html")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def valid_login(self):
        self.login("standard_user", "secret_sauce")
