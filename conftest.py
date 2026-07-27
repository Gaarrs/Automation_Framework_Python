import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.contact_page import ContactPage

@pytest.fixture
def base_page(page):
    return BasePage(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def contact_page(page):
    return ContactPage(page)