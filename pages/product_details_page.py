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
        self.quantity_input = page.locator("#quantity")
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.review_header = page.get_by_text("Write Your Review")
        self.review_name_input = page.locator("#name")
        self.review_email_input = page.locator("#email")
        self.review_text_input = page.get_by_placeholder("Add Review Here!")
        self.review_button = page.locator("#button-review")
        self.review_success_alert = page.get_by_text("Thank you for your review.")

    def send_review(self, name="test-name", email="test-email@mail.com", text="lorem ipsum"):
        self.review_name_input.fill(name)
        self.review_email_input.fill(email)
        self.review_text_input.fill(text)
        self.review_button.click()