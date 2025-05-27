from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.login_page.login_page import LoginPage
from playwright.sync_api import expect

def test_inventory_elements_after_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.valid_login()
    inventory_page = InventoryPage(page)

    # Wait for the container to appear before asserting
    inventory_page.inventory_container.wait_for(state="visible")

    expect(inventory_page.inventory_container).to_be_visible()
    expect(inventory_page.add_to_cart_buttons.first).to_be_visible()
