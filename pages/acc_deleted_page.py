from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class AccDeletedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.acc_deleted_header = self.page.get_by_text("Account Deleted!")
        self.continue_button = self.page.locator("a[data-qa='continue-button']")