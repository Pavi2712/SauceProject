from playwright.sync_api import Page
from saucedemo.pages.cart_page.locators import CartPageLocators

class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(CartPageLocators.CART_ITEMS)
        self.checkout_button = page.locator(CartPageLocators.CHECKOUT_BUTTON)
        self.cart_icon = page.locator(CartPageLocators.CART_ICON)

    def proceed_to_checkout(self):
        self.page.click(CartPageLocators.CHECKOUT_BUTTON)


    def cart_items_exist(self):
        return self.page.locator(CartPageLocators.CART_ITEMS).count() > 0
    
    def open_cart(self):
        self.page.locator(CartPageLocators.CART_ICON).click()
