from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products_list = page.locator(".features_items")
        self.products_details = page.get_by_text("View Product")