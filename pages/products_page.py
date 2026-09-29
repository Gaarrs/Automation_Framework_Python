from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products = page.locator(".features_items")
        self.products_details = page.get_by_text("View Product")
        self.products_list = page.locator(".product-image-wrapper")
        self.products_buttons_list = page.locator(".product-overlay a")
        self.continue_shopping_button = page.get_by_role("button", name="Continue shopping")
        self.view_cart_link = page.get_by_role("link", name="View Cart")

    def add_to_cart(self, product_id):
        self.products_list.nth(product_id).hover()
        self.products_buttons_list.nth(product_id).click()