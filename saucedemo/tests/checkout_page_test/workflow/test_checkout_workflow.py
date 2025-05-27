from saucedemo.pages.cart_page.cart_page import CartPage
from saucedemo.pages.checkout_page.checkout_page import CheckoutPage
from saucedemo.pages.confirmation_page.confirmation_page import ConfirmationPage
from saucedemo.pages.login_page.login_page import LoginPage
from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_checkout_submission(page):
    # Step 1: Login
    login_page = LoginPage(page)
    login_page.goto()
    login_page.valid_login()

    # Step 2: Add item to cart
    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_cart()
    
    # Step 3: Open cart and proceed to checkout
    inventory_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    # Step 4: Fill in checkout form and continue
    checkout_page = CheckoutPage(page)
    checkout_page.fill_and_continue("Pavi", "Test", "600001")

    # Step 5: Verify finish button is visible
    confirmation_page = ConfirmationPage(page)
    confirmation_page.should_have_finish_button()
