from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_email_input = page.locator('[data-qa="login-email"]')
        self.login_password_input = page.locator('[data-qa="login-password"]')
        self.login_button = page.locator('[data-qa="login-button"]')
        self.signup_name_input = page.locator('[data-qa="signup-name"]')
        self.signup_email_input = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.locator('[data-qa="signup-button"]')
        self.signup_header = page.get_by_text("New User Signup!")
        self.login_header = page.get_by_text("Login to your account")

    def open(self):
        LoginPage.navigate(self, "https://automationexercise.com/login")

    def signup(self, name, email):
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_button.click()

    def login(self, email, password):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()