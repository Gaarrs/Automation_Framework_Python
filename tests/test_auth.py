import pytest
import allure
from playwright.sync_api import Page, expect

username = "Morty"
email = "ops@mail.ru"
password = "qwerty123"

@allure.story('Authentication feature')
@allure.title("Register User")
def test_user_registration(login_page, signup_page, acc_created_page, acc_deleted_page):
    with allure.step("Открыть домашнюю страницу"):
        login_page.navigate("https://automationexercise.com/")
    with allure.step("Нажать на ссылку Signup/Login"):
        login_page.login_link.click()
    with allure.step("Проверить, что видно заголовок 'New User Signup!'"):
        expect(login_page.signup_header).to_be_visible()
    with allure.step("Ввести name и email и нажать Signup"):
        login_page.signup(username, email)
    with allure.step("Проверить, что отображается 'ENTER ACCOUNT INFORMATION'"):
        expect(signup_page.info_header).to_be_visible()
    with allure.step("Заполнить информацию об аккаунте"):
        signup_page.acc_info_fill('Mr', username, password, '15', 'March', '1995')
    with allure.step("Активировать чекбокс новостной рассылки"):
        signup_page.news_checkbox.check()
    with allure.step("Активировать чекбокс специальных предложений"):
        signup_page.offers_checkbox.check()
    with allure.step("Заполнить аддресную информацию"):
        signup_page.address_info_fill('John', 'Smith', 'Umbrella corp', 'San-Jose', 'Sacramento', 'United States', 'California', 'Sacramento', '350075', '89991232321' )
    with allure.step("Нажать кнопку Create Account"):
        signup_page.create_button.click()
    with allure.step("Проверить, что отображается 'Account Created!'"):
        expect(acc_created_page.acc_created_header).to_be_visible()
    with allure.step("Нажать кнопку 'Continue'"):
        acc_created_page.continue_button.click()
    with allure.step(f"Проверить, что отображается 'Logged in as {username}'"):
        expect(login_page.logged_status).to_contain_text(f'Logged in as {username}')
        expect(login_page.logged_status).to_be_visible()
    # with allure.step("Нажать на Delete account"):
    #     login_page.delete_acc_link.click()
    # with allure.step("Проверить, что отображается 'Account Deleted!'"):
    #     expect(acc_deleted_page.acc_deleted_header).to_be_visible()
    # with allure.step("Нажать на кнопку 'Continue'"):
    #     acc_deleted_page.continue_button.click()

@allure.story('Authentication feature')
@allure.title("Logout User")
def test_user_logout(login_page, page):
    with allure.step("Открыть домашнюю страницу"):
        login_page.navigate("https://automationexercise.com/")
    with allure.step("Нажать на ссылку Signup/Login"):
        login_page.login_link.click()
    with allure.step("Проверить, что отображается заголовок 'Login to your account'"):
        expect(login_page.login_header).to_be_visible()
    with allure.step("Выполнить логин с корректными данными"):
        login_page.login(email, password)
    with allure.step(f"Проверить, что отображается 'Logged in as {username}'"):
        expect(login_page.logged_status).to_contain_text(f'Logged in as {username}')
        expect(login_page.logged_status).to_be_visible()
    with allure.step("Нажать на кнопку Logout"):
        login_page.logout_link.click()
    with allure.step("Проверить, что пользователя вернуло на Login Page"):
        expect(page).to_have_url("https://automationexercise.com/login")

@allure.story('Authentication feature')
@allure.title("Login User with correct email and password")
def test_user_login_correct(login_page, acc_deleted_page):
    with allure.step("Открыть домашнюю страницу"):
        login_page.navigate("https://automationexercise.com/")
    with allure.step("Нажать на ссылку Signup/Login"):
        login_page.login_link.click()
    with allure.step("Проверить, что отображается заголовок 'Login to your account'"):
        expect(login_page.login_header).to_be_visible()
    with allure.step("Выполнить логин с корректными данными"):
        login_page.login(email, password)
    with allure.step(f"Проверить, что отображается 'Logged in as {username}'"):
        expect(login_page.logged_status).to_contain_text(f'Logged in as {username}')
        expect(login_page.logged_status).to_be_visible()
    with allure.step("Нажать на Delete account"):
        login_page.delete_acc_link.click()
    with allure.step("Проверить, что отображается 'Account Deleted!'"):
        expect(acc_deleted_page.acc_deleted_header).to_be_visible()

@allure.story('Authentication feature')
@allure.title("Login User with incorrect email and password")
def test_user_login_incorrect(login_page, acc_deleted_page):
    with allure.step("Открыть домашнюю страницу"):
        login_page.navigate("https://automationexercise.com/")
    with allure.step("Нажать на ссылку Signup/Login"):
        login_page.login_link.click()
    with allure.step("Проверить, что отображается заголовок 'Login to your account'"):
        expect(login_page.login_header).to_be_visible()
    with allure.step("Попробовать залогиниться с некорректными данными"):
        login_page.login("incorrect@email.ru", "password_incorrect")
    with allure.step("Проверить, что отображается сообщение о некорректных данных для входа"):
        expect(login_page.incorrect_alert).to_be_visible()





