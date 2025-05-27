from saucedemo.pages.login_page.login_page import LoginPage
from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.cart_page.cart_page import CartPage
from playwright.sync_api import expect

def test_cart_page_elements(page):
    # Login first
    login_page = LoginPage(page)
    login_page.goto()
    login_page.valid_login()

    # Add at least one item to cart from inventory
    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_cart()  # Make sure this clicks the add to cart button

    # Open cart page
    cart_page = CartPage(page)
    cart_page.open_cart()

    # Now assert cart items are visible (since you added one)
    expect(cart_page.cart_items).to_be_visible()
    expect(cart_page.checkout_button).to_be_visible()
