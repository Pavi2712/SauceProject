from saucedemo.pages.cart_page.cart_page import CartPage
from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.login_page.login_page import LoginPage
from playwright.sync_api import expect

def test_add_item_to_cart(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.valid_login()
    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_cart()
    cart_page = CartPage(page)
    cart_page.open_cart()
    expect(cart_page.cart_items).to_have_count(1)