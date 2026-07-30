from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = page.url
        self.logo = page.get_by_alt_text("Website for automation practice")
        self.home_link = page.locator('a[href="/"]')
        self.products_link = page.locator('a[href="/products"]')
        self.cart_link = page.locator('a[href="/view_cart"]')
        self.login_link = page.locator('a[href="/login"]')
        self.tests_link = page.locator('a[href="/test_cases"]')
        self.api_link = page.locator('a[href="/api_list"]')
        self.contact_link = page.locator('a[href="/contact_us"]')
        self.logout_link = page.locator('a[href="/logout"]')
        self.delete_acc_link = page.locator('a[href="/delete_account"]')
        self.logged_status = page.locator("a:text('Logged')")
        self.sub_input = page.get_by_placeholder("Your email address")
        self.sub_button = page.locator("#subscribe")
        self.scroll_button = page.locator("#scrollUp")

    def navigate(self, url: str):
        self.page.goto(url, timeout=60000)

    def open_cart(self):
        self.cart_button.click()

    def subscription(self, email: str):
        self.sub_input.fill(email)
        self.sub_button.click()

    def scroll_up(self):
        self.scroll_button.click()