import pytest
from pages.login_page.login_page import LoginPage
from pages.inventory_page.inventory_page import InventoryPage
from pages.cart_page.cart_page import CartPage


def test_proceed_to_checkout(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.valid_login()

    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()
    assert "checkout-step-one" in page.url
