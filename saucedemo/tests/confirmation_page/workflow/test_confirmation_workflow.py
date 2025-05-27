from saucedemo.pages.login_page.login_page import LoginPage
from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.cart_page.cart_page import CartPage
from saucedemo.pages.checkout_page.checkout_page import CheckoutPage
from saucedemo.pages.confirmation_page.confirmation_page import ConfirmationPage
from playwright.sync_api import expect

def test_order_completion(page):
    # Step 1: Login
    login_page = LoginPage(page)
    login_page.goto()
    login_page.valid_login()

    # Step 2: Add item to cart
    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_cart()

    # Step 3: Proceed to cart
    cart_page = CartPage(page)
    cart_page.open_cart()
    cart_page.proceed_to_checkout()

    # Step 4: Fill checkout info
    checkout_page = CheckoutPage(page)
    checkout_page.fill_and_continue("Pavi", "Test", "600001")

    # Step 5: Complete order
    confirmation_page = ConfirmationPage(page)
    confirmation_page.complete_order()

    # Step 6: Assert order confirmation message
    expect(confirmation_page.confirmation_message).to_contain_text("Thank you for your order!")
