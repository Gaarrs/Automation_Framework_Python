import allure
from playwright.sync_api import Page, expect

from pages.product_details_page import ProductDetailsPage


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
        expect(products_page.products).to_be_visible()
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

@allure.story("Products")
@allure.title("Add Products in Cart")
def test_add_products_to_cart(products_page, view_cart_page, base_page, page):
    with allure.step("Открыть домашнюю страницу"):
        base_page.navigate("https://automationexercise.com/")
    with allure.step("Кликнуть на ссылку Products"):
        base_page.products_link.click()
    with allure.step("Навести курсор на продукт 1 и добавить его в корзину"):
        products_page.add_to_cart(0)
    with allure.step("Нажать кнопку 'Continue shopping'"):
        products_page.continue_shopping_button.click()
    with allure.step("Навести курсор на продукт 2 и добавить его в корзину"):
        products_page.add_to_cart(1)
    with allure.step("Нажать кнопку 'View cart'"):
        products_page.view_cart_link.click()
    with allure.step("Проверить, что оба продукта добавлены в корзину"):
        expect(view_cart_page.incart_products_list).to_have_count(2)
    with allure.step("Проверить соответствие цены, количества и общей цены"):
        view_cart_page.verify_price_quantity()

@allure.story("Products")
@allure.title("Search Product")
def test_search_product(base_page, products_page, view_cart_page, page):
    with allure.step("Открыть домашнюю страницу"):
        base_page.navigate("https://automationexercise.com/")
    with allure.step("Кликнуть на ссылку Products"):
        base_page.products_link.click()
    with allure.step("Проверить, что юзер оказался на странице Products"):
        expect(page).to_have_url("https://automationexercise.com/products")
    with allure.step("Ввести критерий поиска в поле Search и нажать на кнопку поиска"):
        products_page.search("Jeans")
    with allure.step("Проверить, что отображаются товары, удовлетворяющие критерию поиска"):
        products_page.verify_search("Jeans")