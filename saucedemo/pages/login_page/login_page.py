from saucedemo.pages.login_page.locators import LoginPageLocators

class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")

    def valid_login(self):
        self.page.fill(LoginPageLocators.USERNAME_INPUT, "standard_user")
        self.page.fill(LoginPageLocators.PASSWORD_INPUT, "secret_sauce")
        self.page.click(LoginPageLocators.LOGIN_BUTTON)
