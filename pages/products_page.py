from .base_page import BasePage


class ProductsPage(BasePage):
    PRODUCTS_PAGE_IDENTIFIER = "h2.title:has-text('All Products')"
    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    SEARCHED_PRODUCTS_TITLE = "h2.title:has-text('Searched Products')"
    SEARCH_RESULTS = ".features_items .product-image-wrapper"

    def verify_products_page_visible(self):
        return self.is_visible(self.PRODUCTS_PAGE_IDENTIFIER)

    def search_product(self, name):
        self.fill(self.SEARCH_INPUT, name)
        self.click(self.SEARCH_BUTTON)

    def verify_searched_products_title(self):
        return self.is_visible(self.SEARCHED_PRODUCTS_TITLE)

    def verify_search_results_visible(self):
        return self.is_visible(self.SEARCH_RESULTS)
