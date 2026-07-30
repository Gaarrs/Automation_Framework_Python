from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class AccCreatedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.acc_created_header = self.page.get_by_text("Account Created!")
        self.continue_button = self.page.locator("a[data-qa='continue-button']")