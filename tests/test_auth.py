import pytest
import allure
from playwright.sync_api import Page, expect


@allure.story('Authentication feature')
@allure.title("Register User")
def test_user_registration(login_page):
    with allure.step("Открыть домашнюю страницу"):
        login_page.navigate("https://automationexercise.com/")
    with allure.step("Нажать на ссылку Signup/Login"):
        login_page.login_link.click()
    with allure.step("Проверить, что видно заголовок 'New User Signup!'"):
        expect(login_page.signup_header).to_be_visible()
    with allure.step("Ввести name и email и нажать Signup"):
        login_page.signup("ars","ars@mail.com")
