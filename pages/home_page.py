from .base_page import BasePage


class HomePage(BasePage):
    HOME_PAGE_IDENTIFIER = "div.features_items"
    PRODUCTS_BUTTON = "a[href='/products']"
    FIRST_PRODUCT_VIEW = (
        ".features_items .product-image-wrapper:first-child a[href*='/product_details']"
    )

    def verify_home_page_visible(self):
        return self.is_visible(self.HOME_PAGE_IDENTIFIER)

    def click_products_button(self):
        self.click(self.PRODUCTS_BUTTON)

    def click_first_product(self):
        self.click(self.FIRST_PRODUCT_VIEW)
