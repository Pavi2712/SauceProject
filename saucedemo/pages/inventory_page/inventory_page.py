from playwright.sync_api import Page
from saucedemo.pages.inventory_page.locators import InventoryPageLocators

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_container = page.locator(InventoryPageLocators.INVENTORY_CONTAINER)

    @property
    def add_to_cart_buttons(self):
        return self.page.locator(InventoryPageLocators.ADD_TO_CART_BUTTONS)      

    def add_first_item_to_cart(self):
        self.page.wait_for_selector(InventoryPageLocators.FIRST_ITEM_ADD_BUTTON)
        self.page.click(InventoryPageLocators.FIRST_ITEM_ADD_BUTTON)

    def go_to_cart(self):
        self.page.click(InventoryPageLocators.CART_ICON)

        

    
