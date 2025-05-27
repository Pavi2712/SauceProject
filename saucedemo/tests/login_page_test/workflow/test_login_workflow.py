from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.login_page.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.valid_login()
    
    inventory_page = InventoryPage(page)
    assert inventory_page.page.locator('[id="inventory_container"] :has([id="inventory_container"])').is_visible()