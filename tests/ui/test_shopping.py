import allure
from playwright.sync_api import Page, expect

@allure.story("Products")
@allure.title("Verify All Products and product detail page")
def test_products_page_details(products_page, product_details_page, base_page, page):
    with allure.step("Открыть домашнюю страницу"):
        base_page.navigate("https://automationexercise.com/")
    with allure.step("Кликнуть на ссылку Products"):
        base_page.products_link.click()
    with allure.step("Проверить, что юзер оказался на странице Products"):
        expect(page).to_have_url("https://automationexercise.com/products")
    with allure.step("Проверить, что отображается список продуктов"):
        expect(products_page.products_list).to_be_visible()
    with allure.step("Нажать на кнопку подробной информации у первого продукта"):
        (products_page.products_details.first).click()
    with allure.step("Проверить , что юзера перенаправило на страницу деталей о продукте"):
        expect(page).to_have_url("https://automationexercise.com/product_details/1")
    with allure.step("Проверить, что отображаются product name"):
        expect(product_details_page.product_name).to_be_visible()
    with allure.step("Проверить, что отображаются category"):
        expect(product_details_page.product_category).to_be_visible()
    with allure.step("Проверить, что отображаются price"):
        expect(product_details_page.product_price).to_be_visible()
    with allure.step("Проверить, что отображаются availability"):
        expect(product_details_page.product_availability).to_be_visible()
    with allure.step("Проверить, что отображаются condition"):
        expect(product_details_page.product_condition).to_be_visible()
    with allure.step("Проверить, что отображаются brand"):
        expect(product_details_page.product_brand).to_be_visible()