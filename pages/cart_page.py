from .base_page import BasePage


class CartPage(BasePage):
    MODAL = "#cartModal"
    VIEW_CART_BTN_IN_MODAL = "#cartModal a[href='/view_cart']"
    CART_QUANTITY_CELL = ".cart_quantity button"

    def open_cart(self):
        self.page.wait_for_selector(self.MODAL, state="visible", timeout=5000)
        self.page.wait_for_selector(
            self.VIEW_CART_BTN_IN_MODAL, state="visible", timeout=5000
        )
        self.click(self.VIEW_CART_BTN_IN_MODAL)

    def verify_quantity(self, expected_qty):
        qty_text = self.page.inner_text(self.CART_QUANTITY_CELL).strip()
        return str(expected_qty) == qty_text
