from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        # Correct complex selector based on your input
        self.inventory_container = page.locator('[id="inventory_container"] :has([id="inventory_container"])')
        self.add_to_cart_buttons = page.locator(".btn_inventory")
