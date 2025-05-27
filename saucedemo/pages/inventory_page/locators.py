class InventoryPageLocators:
    INVENTORY_CONTAINER = '[id="inventory_container"]:has([id="inventory_container"])'
    FIRST_ITEM_ADD_BUTTON = "button[data-test='add-to-cart-sauce-labs-backpack']"
    ADD_TO_CART_BUTTONS = 'button[data-test^="add-to-cart"]'  # Matches all add-to-cart buttons
    CART_ICON = '.shopping_cart_link'