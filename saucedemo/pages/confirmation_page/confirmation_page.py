from playwright.sync_api import Page
from saucedemo.pages.confirmation_page.locators import ConfirmationPageLocators
from playwright.sync_api import expect

class ConfirmationPage:
    def __init__(self, page):
        self.page = page

    def complete_order(self):
        self.page.click(ConfirmationPageLocators.FINISH_BUTTON)
        self.page.wait_for_timeout(1000)

    def should_have_finish_button(self):
        expect(self.page.locator(ConfirmationPageLocators.FINISH_BUTTON)).to_be_visible()

    def should_have_summary_container(self):
        expect(self.page.locator(ConfirmationPageLocators.SUMMARY_CONTAINER)).to_be_visible()

    @property
    def finish_button(self):
        return self.page.locator(ConfirmationPageLocators.FINISH_BUTTON)
    
    @property
    def summary_container(self):
        return self.page.locator(ConfirmationPageLocators.SUMMARY_CONTAINER)

    @property
    def confirmation_message(self):
        return self.page.locator(ConfirmationPageLocators.ORDER_CONFIRMATION_TEXT)