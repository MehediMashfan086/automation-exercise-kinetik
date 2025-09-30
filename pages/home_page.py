from .base_page import BasePage


class HomePage(BasePage):
    HOME_PAGE_IDENTIFIER = "div.features_items"
    PRODUCTS_BUTTON = "a[href='/products']"

    def verify_home_page_visible(self):
        return self.is_visible(self.HOME_PAGE_IDENTIFIER)

    def click_products_button(self):
        self.click(self.PRODUCTS_BUTTON)
