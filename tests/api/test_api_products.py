import allure
import pytest
from uuid import uuid4

from conftest import api_request

account = {
        'name': 'Axel',
        'email': f'{uuid4().hex}@mail.com',
        'password': uuid4().hex,
        'title': 'Mr',
        'birth_date': '15',
        'birth_month': 'March',
        'birth_year': '1995',
        'firstname': 'Axel',
        'lastname': 'Jonson',
        'company': 'X',
        'address1': 'San Jose',
        'address2': 'Los Angeles',
        'country': 'USA',
        'zipcode': '139923',
        'state': 'California',
        'city': 'San Diego',
        'mobile_number': '891833355523'
    }

@pytest.fixture
def created_account(api_request):
    account = {
        'name': 'Alexis',
        'email': f'{uuid4().hex}@mail.com',
        'password': uuid4().hex,
        'title': 'Mrs',
        'birth_date': '15',
        'birth_month': 'March',
        'birth_year': '1995',
        'firstname': 'Alexis',
        'lastname': 'Jonson',
        'company': 'X',
        'address1': 'San Jose',
        'address2': 'Los Angeles',
        'country': 'USA',
        'zipcode': '139923',
        'state': 'California',
        'city': 'San Diego',
        'mobile_number': '891833355523'
    }

    response = api_request.post("/api/createAccount", form=account)
    assert response.ok, f"Ошибка создания аккаунта: HTTP {response.status}"
    assert response.json()['responseCode'] == 201, response.text()

    yield account

    response = api_request.delete("/api/deleteAccount", form={"email":account['email'], "password":account['password']})
    assert response.ok, f"Ошибка удаления аккаунта: HTTP {response.status}"
    assert response.json()['responseCode'] == 200, response.text()


@allure.story('API tests')
@allure.title("Get All Products List")
def test_api_products_get(api_request):
    response = api_request.get("/api/productsList")

    assert response.ok, f"Ошибка получения списка товаров: HTTP {response.status}"
    assert response.status == 200, f'Статус ответа: {response.status}'
    json_data = response.json()
    all_products_list = json_data["products"]
    assert isinstance(all_products_list, list)
    assert len(json_data['products']) > 0

@allure.story('API tests')
@allure.title("Post to All Products List")
def test_api_products_post(api_request):
    response = api_request.post("/api/productsList", data={'test':'data'})

    data = response.json()
    assert response.ok
    assert data['responseCode'] == 405
    assert data['message'] == "This request method is not supported."

@allure.story('API tests')
@allure.title("Get All Brands List")
def test_api_brands_get(api_request):
    response = api_request.get("/api/brandsList")

    assert response.ok
    data = response.json()
    brands_list = data["brands"]
    assert isinstance(brands_list, list)
    assert len(brands_list) > 0

@allure.story('API tests')
@allure.title("Put to All Brands List")
def test_api_brands_put(api_request):
    response = api_request.put("/api/brandsList")

    data = response.json()
    assert response.ok
    assert data['responseCode'] == 405
    assert data['message'] == "This request method is not supported."

@allure.story('API tests')
@allure.title("POST To Create/Register User Account")
def test_api_create_account(api_request):
    response = api_request.post("/api/createAccount", form=account)
    data = response.json()

    assert response.ok, f"Ошибка создания аккаунта: HTTP {response.status}"
    assert data['responseCode'] == 201, response.text()
    assert data['message'] == "User created!"

    response = api_request.get("/api/getUserDetailByEmail", params={"email":account["email"]})
    user = response.json()["user"]
    assert user["email"] == account["email"]
    assert user["name"] == account["name"]

    response = api_request.delete("/api/deleteAccount",
                                  form={"email": account['email'], "password": account['password']})


@allure.story('API tests')
@allure.title("PUT METHOD To Update User Account")
def test_api_update_account(api_request, created_account):
    updated_account = {**created_account, "name":"Updated Name", "birth_year":"1998"}

    response = api_request.put("/api/updateAccount", form=updated_account)
    assert response.ok, f"HTTP: {response.status}"

    data = response.json()
    assert data['responseCode'] == 200, response.text()
    assert data['message'] == "User updated!"

    response = api_request.get("/api/getUserDetailByEmail", params={'email':created_account['email']})
    assert response.ok, f"HTTP: {response.status}"

    user = response.json()["user"]
    assert user["name"] == updated_account["name"]
    assert user["birth_year"] == updated_account["birth_year"]

@allure.story('API tests')
@allure.title("GET user account detail by email")
def test_api_get_acc_info(api_request, created_account):
    response = api_request.get('/api/getUserDetailByEmail', params={'email':created_account['email']})
    data = response.json()

    assert response.ok
    assert response.status == 200
    assert data['user']['name'] == created_account['name']
    assert data['user']['birth_year'] == created_account['birth_year']

@allure.story('API tests')
@allure.title("DELETE METHOD To Delete User Account")
def test_api_delete_account(api_request):
    response = api_request.post("/api/createAccount", form=account)
    data = response.json()

    assert response.ok, f"Ошибка создания аккаунта: HTTP {response.status}"
    assert data['responseCode'] == 201, response.text()
    assert data['message'] == "User created!"

    response = api_request.delete("/api/deleteAccount",
                                  form={"email": account['email'], "password": account['password']})
    assert response.ok, f"HTTP: {response.status}"

    data = response.json()
    assert data['responseCode'] == 200, response.text()
    assert data['message'] == 'Account deleted!'