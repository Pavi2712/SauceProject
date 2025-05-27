from saucedemo.pages.cart_page.cart_page import CartPage
from saucedemo.pages.checkout_page.checkout_page import CheckoutPage, CheckoutPageLocators
from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.login_page.login_page import LoginPage
from playwright.sync_api import expect

def test_checkout_elements(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.valid_login()
    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_cart()
    cart_page = CartPage(page)
    cart_page.open_cart()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.should_have_first_name_input()
    checkout_page.should_have_last_name_input()
    checkout_page.should_have_postal_code_input()