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
        self.days_select = "#days"
        self.months_select = "#months"
        self.years_select = "#years"
        self.news_checkbox = page.locator("#newsletter")
        self.offers_checkbox = page.locator("#optin")
        self.address_header = page.get_by_text("Address Information")
        self.first_name_input = page.locator("input[data-qa='first_name']")
        self.last_name_input = page.locator("input[data-qa='last_name']")
        self.company_input = page.locator("#company")
        self.address1_input = page.locator("#address1")
        self.address2_input = page.locator("input[data-qa='address2']")
        self.country_select = "#country"
        self.state_input = page.locator("#state")
        self.city_input = page.locator("#city")
        self.zip_input = page.locator("input[data-qa='zipcode']")
        self.mobile_input = page.locator("#mobile_number")
        self.create_button = page.locator("button[data-qa='create-account']")

    def acc_info_fill(self, title, name, password, day, month, year):
        if title=='Mr':
            self.mr_radio.check()
        elif title=='Mrs':
            self.mrs_radio.check()
        self.info_name_input.fill(name)
        self.info_password_input.fill(password)
        self.page.select_option(self.days_select, value = day)
        self.page.select_option(self.months_select, value = month)
        self.page.select_option(self.years_select, value = year)

    def address_info_fill(self, first_name, last_name, company, address1, address2, country, state, city, zip_code, mobile):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.company_input.fill(company)
        self.address1_input.fill(address1)
        self.address2_input.fill(address2)
        self.page.select_option(self.country_select, value = country)
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zip_input.fill(zip_code)
        self.mobile_input.fill(mobile)