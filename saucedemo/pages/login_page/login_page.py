from saucedemo.pages.login_page.locators import LoginPageLocators
from saucedemo.pages.login_page.constants import LOGIN_URL, USERNAME, PASSWORD

class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(LOGIN_URL)

    def valid_login(self):
        self.page.fill(LoginPageLocators.USERNAME_INPUT, USERNAME)
        self.page.fill(LoginPageLocators.PASSWORD_INPUT, PASSWORD)
        self.page.click(LoginPageLocators.LOGIN_BUTTON)
