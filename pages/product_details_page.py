from pages.products_page import ProductsPage

class ProductDetailsPage(ProductsPage):
    def __init__(self, page):
        super().__init__(page)
        self.product_name = page.locator(".product-information h2")
        self.product_category = page.locator(".product-information p:text('Category:')")
        self.product_price = page.get_by_text("Rs.")
        self.product_availability = page.locator(".product-information b:text('Availability:')")
        self.product_condition = page.locator(".product-information b:text('Condition:')")
        self.product_brand = page.locator(".product-information b:text('Brand:')")