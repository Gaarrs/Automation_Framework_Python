from playwright.sync_api import Page
import os
from pages.base_page import BasePage

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "file.txt")

class ContactPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.contact_header = page.get_by_text("Get In Touch")
        self.contact_name = page.locator("input[data-qa='name']")
        self.contact_email = page.locator("input[data-qa='email']")
        self.contact_subject = page.get_by_placeholder("Subject")
        self.contact_message = page.locator("#message")
        self.submit = page.locator("input[data-qa='submit-button']")
        self.upload = page.locator("[name='upload_file']")
        self.success_alert = page.locator("#contact-page").get_by_text("Success! Your details have")
        self.home_button = page.locator("span:text(' Home')")

    def contact_form_fill(self, name, email, subject, message):
        press_delay = 50
        self.contact_name.press_sequentially(name, delay=press_delay)
        self.contact_email.press_sequentially(email, delay=press_delay)
        self.contact_subject.press_sequentially(subject, delay=press_delay)
        self.contact_message.press_sequentially(message, delay=press_delay)
        self.upload.set_input_files(file_path)