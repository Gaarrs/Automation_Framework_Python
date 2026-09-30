from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.get_by_placeholder("Search Product")
        self.search_button = page.locator("#submit_search")
        self.searched_products_heading = page.get_by_role("heading", name="Searched Products")
        self.products = page.locator(".features_items")
        self.products_details = page.get_by_text("View Product")
        self.products_list = page.locator(".product-image-wrapper")
        self.products_names_list = page.locator(".product-image-wrapper p")
        self.products_buttons_list = page.locator(".product-overlay a")
        self.continue_shopping_button = page.get_by_role("button", name="Continue shopping")
        self.view_cart_link = page.get_by_role("link", name="View Cart")

    def add_to_cart(self, product_id):
        self.products_list.nth(product_id).hover()
        self.products_buttons_list.nth(product_id).click()

    def search(self, search_criteria):
        self.search_input.fill(search_criteria)
        self.search_button.click()

    def verify_search(self, search_criteria):
        count = self.products_names_list.count() - 1
        while count >= 0:
            expect(self.products_names_list.nth(count)).to_contain_text(search_criteria)
            count -= 1