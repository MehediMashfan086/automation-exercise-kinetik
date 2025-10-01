from .base_page import BasePage


class ProductPage(BasePage):
    QUANTITY_INPUT = "input#quantity"
    ADD_TO_CART_BTN = "button.cart"

    def verify_product_detail_visible(self):
        return self.is_visible(self.QUANTITY_INPUT)

    def set_quantity(self, qty):
        self.fill(self.QUANTITY_INPUT, str(qty))

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
        self.page.wait_for_selector("#cartModal", state="visible", timeout=5000)
