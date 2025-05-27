from saucedemo.pages.cart_page.cart_page import CartPage
from saucedemo.pages.checkout_page.checkout_page import CheckoutPage
from saucedemo.pages.confirmation_page.confirmation_page import ConfirmationPage
from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.login_page.login_page import LoginPage

def test_confirmation_page_elements(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.valid_login()
    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_cart()
    cart_page = CartPage(page)
    cart_page.open_cart()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.fill_and_continue("Pavi", "Test", "600001")
    confirmation_page = ConfirmationPage(page)
    confirmation_page.should_have_finish_button()
    confirmation_page.should_have_summary_container()