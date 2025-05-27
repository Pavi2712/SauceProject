from playwright.sync_api import Page, expect
from saucedemo.pages.checkout_page.locators import CheckoutPageLocators

class CheckoutPage:
    def __init__(self, page):
        self.page = page
    
    def should_have_first_name_input(self):
        expect(self.page.locator(CheckoutPageLocators.FIRST_NAME_INPUT)).to_be_visible()
    def should_have_last_name_input(self):
        expect(self.page.locator(CheckoutPageLocators.LAST_NAME_INPUT)).to_be_visible()
    def should_have_postal_code_input(self):
        expect(self.page.locator(CheckoutPageLocators.POSTAL_CODE_INPUT)).to_be_visible()

    def fill_and_continue(self, first_name, last_name, postal_code):
        self.page.fill(CheckoutPageLocators.FIRST_NAME_INPUT, first_name)
        self.page.fill(CheckoutPageLocators.LAST_NAME_INPUT, last_name)
        self.page.fill(CheckoutPageLocators.POSTAL_CODE_INPUT, postal_code)
        self.page.click(CheckoutPageLocators.CONTINUE_BUTTON)
        self.page.wait_for_timeout(2000)

    @property
    def checkout_form(self):
        return self.page.locator(CheckoutPageLocators.FIRST_NAME_INPUT)