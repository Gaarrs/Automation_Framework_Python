from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class SignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.info_header = page.get_by_text("Enter Account Information")