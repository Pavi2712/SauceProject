import pytest
from playwright.sync_api import expect
from saucedemo.loginpage.loginpage import LoginPage
from saucedemo.loginpage.productspage import ProductsPage

@pytest.fixture(scope="function")
def login_page(page):
    # Use headed mode and set viewport
    page.set_viewport_size({"width": 1280, "height": 800})
    return LoginPage(page)

def test_ui_elements_visibility_and_content(login_page):
    page = login_page.page
    login_page.goto()

    # Validate login page elements
    expect(login_page.logo).to_be_visible()
    expect(login_page.username_input).to_be_visible()
    expect(login_page.username_input).to_have_attribute("placeholder", "Username")

    expect(login_page.password_input).to_be_visible()
    expect(login_page.password_input).to_have_attribute("placeholder", "Password")

    expect(login_page.login_button).to_be_visible()
    expect(login_page.login_button).to_have_text("LOGIN")
    expect(login_page.login_button).to_be_enabled()

    expect(login_page.form_container).to_be_visible()
    expect(login_page.bot_image).to_be_visible()

    expect(login_page.cred_section).to_contain_text("standard_user")
    expect(login_page.password_section).to_contain_text("secret_sauce")

    expect(login_page.username_input).to_have_value("")
    expect(login_page.password_input).to_have_value("")

    # Perform login
    login_page.login("standard_user", "secret_sauce")

    # Add 5-second wait
    page.wait_for_timeout(5000)

    # Product page assertions
    products_page = ProductsPage(page)
    expect(products_page.inventory_container).to_be_visible()
    expect(products_page.add_to_cart_buttons.first).to_be_enabled()
