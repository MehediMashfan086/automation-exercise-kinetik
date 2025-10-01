import time

import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from utils import config, logger, test_data

log = logger.get_logger()


@pytest.mark.parametrize("quantity", [test_data.TEST_DATA.get("quantity", 1)])
def test_add_product_to_cart(setup, quantity):
    page = setup

    log.info("Navigate to homepage.....")
    home = HomePage(page)
    home.goto(config.BASE_URL)
    assert home.verify_home_page_visible(), "Home page not visible"

    log.info("Click the first product (View Product).....")
    home.click_first_product()

    product = ProductPage(page)
    assert product.verify_product_detail_visible(), "Product detail page not visible"

    log.info(f"Set quantity to {quantity}.....")
    product.set_quantity(quantity)

    log.info("Click Add to cart.....")
    product.add_to_cart()
    time.sleep(1)

    cart = CartPage(page)
    log.info("Open cart / view cart.....")
    cart.open_cart()
    time.sleep(3)

    log.info("Verify product quantity in cart.....")
    assert cart.verify_quantity(quantity), f"Expected quantity {quantity} in cart"
