import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.contact_page import ContactPage
from pages.signup_page import SignupPage
from pages.acc_created_page import AccCreatedPage
from pages.acc_deleted_page import AccDeletedPage

@pytest.fixture
def base_page(page):
    return BasePage(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def contact_page(page):
    return ContactPage(page)

@pytest.fixture
def signup_page(page):
    return SignupPage(page)

@pytest.fixture
def acc_created_page(page):
    return AccCreatedPage(page)

@pytest.fixture
def acc_deleted_page(page):
    return AccDeletedPage(page)