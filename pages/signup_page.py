from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class SignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.info_header = page.get_by_text("Enter Account Information")
        self.mr_radio = page.locator("#id_gender1")
        self.mrs_radio = page.locator("#id_gender2")
        self.info_name_input = page.locator("#name")
        self.info_password_input = page.locator("#password")
        self.days_select = page.locator("#days")
        self.months_select = page.locator("#months")
        self.years_select = page.locator("#years")
        self.news_checkbox = page.locator("#newsletter")
        self.offers_checkbox = page.locator("#optin")
        self.address_header = page.get_by_text("Address Information")
        self.first_name_input = page.locator("input[data-qa='first_name']")
        self.last_name_input = page.locator("input[data-qa='last_name']")
        self.company_input = page.locator("#company")
        self.address1_input = page.locator("#address1")
        self.address2_input = page.locator("input[data-qa='address2']")
        self.country_select = page.locator("#country")
        self.state_input = page.locator("#state")
        self.city_input = page.locator("#city")
        self.zip_input = page.locator("input[data-qa='zipcode']")
        self.mobile_input = page.locator("#mobile_number")
        self.create_button = page.locator("button[data-qa='create-account']")