from pages.base_page import BasePage

class ViewCartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.incart_products_list = page.get_by_role("row", name="Product")
        self.incart_products_price_list = page.locator(".cart_price p")
        self.incart_products_total_list = page.locator(".cart_total_price")
        self.incart_products_quantity = page.locator(".cart_quantity button")

    def verify_price_quantity(self):
        count = self.incart_products_list.count() - 1
        while count >= 0:
            assert self.incart_products_price_list.nth(count).inner_text() == self.incart_products_total_list.nth(count).inner_text()
            assert self.incart_products_quantity.nth(count).inner_text() == "1"
            count -= 1