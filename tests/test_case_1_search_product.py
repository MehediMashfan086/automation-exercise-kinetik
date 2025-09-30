import time

import pytest

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils import config, logger, test_data

log = logger.get_logger()


@pytest.mark.parametrize("search_term", test_data.TEST_DATA["search_terms"])
def test_search_products(setup, search_term):
    page = setup

    log.info("Navigating to homepage.....")
    home = HomePage(page)
    home.goto(config.BASE_URL)
    assert home.verify_home_page_visible(), "Home page not visible"

    log.info("Clicking on 'Products' button.....")
    home.click_products_button()
    products = ProductsPage(page)
    assert products.verify_products_page_visible(), "Products page not visible"

    log.info(f"Searching for product: {search_term}")
    products.search_product(search_term)

    log.info("Scrolling down for 3 seconds to view results.....")
    start_time = time.time()
    while time.time() - start_time < 3:
        page.mouse.wheel(0, 300)
        time.sleep(0.5)

    log.info("Verifying 'Searched Products' title is visible.....")
    assert (
        products.verify_searched_products_title()
    ), "'Searched Products' title missing"

    log.info("Verifying search results are displayed.....")
    assert (
        products.verify_search_results_visible()
    ), "No products found in search results"
