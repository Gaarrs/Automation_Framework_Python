from playwright.sync_api import Page, expect
from base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        login_email = page.locator('[data-qa="login-email"]')
        login_password = page.locator('[data-qa="login-password"]')
        login_button = page.olcator('[data-qa="login-button"]')
        signup_name = page.locator('[data-qa="signup-name"]')
        signup_email = page.locator('[data-qa="signup-email"')
        signup_button = page.locator('[data-qa="signup-button"]')