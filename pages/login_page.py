from playwright.sync_api import Page, expect
from base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_email = page.locator('[data-qa="login-email"]')
        self.login_password = page.locator('[data-qa="login-password"]')
        self.login_button = page.locator('[data-qa="login-button"]')
        self.signup_name = page.locator('[data-qa="signup-name"]')
        self.signup_email = page.locator('[data-qa="signup-email"')
        self.signup_button = page.locator('[data-qa="signup-button"]')

    def open(self):
        LoginPage.navigate(self, "https://automationexercise.com/login")

    def signup(self, name, email):
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()

    def login(self, email, password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()