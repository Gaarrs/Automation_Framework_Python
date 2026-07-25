from playwright.sync_api import Page
from base_page import BasePage

class ContactPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.contact_name = page.locator("input[data-qa='name']")
        self.contact_email = page.locator("input[data-qa='email']")
        self.contact_subject = page.get_by_placeholder("Subject")
        self.contact_message = page.get_by_id("message")
        self.submit = page.locator("input[data-qa='submit-button']")
        self.upload = page.locator(".form-control")
