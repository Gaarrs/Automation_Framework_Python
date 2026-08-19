import allure

@allure.story('API tests')
@allure.title("Get All Products List")
def test_api_products_get(api_request):
    response = api_request.get("/api/productsList")

    assert response.ok
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
    payload = {
        'name':'Alexis',
        'email':'aallee@mail.com',
        'password':'12345678',
        'title':'Mrs',
        'birth_date':'15',
        'birth_month':'March',
        'birth_year':'1995',
        'firstname':'Alexis',
        'lastname':'Jonson',
        'company':'X',
        'address1':'San Jose',
        'address2':'Los Angeles',
        'country':'USA',
        'zipcode':'139923',
        'state':'California',
        'city':'San Diego',
        'mobile_number':'891833355523'
    }
    response = api_request.post("/api/createAccount", form=payload)
    data = response.json()

    assert response.ok
    assert data['responseCode'] == 201
    assert data['message'] == "User created!"

    #print(response.text())

@allure.story('API tests')
@allure.title("PUT METHOD To Update User Account")
def test_api_update_account(api_request):
    payload = {
        'name': 'Alexeich',
        'email': 'aallee@mail.com',
        'password': '12345678',
        'title': 'Mrs',
        'birth_date': '15',
        'birth_month': 'March',
        'birth_year': '2005',
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
    response = api_request.put("/api/updateAccount", form=payload)
    data = response.json()

    assert response.ok
    assert data['responseCode'] == 200
    assert data['message'] == "User updated!"

    #print(response.text())

@allure.story('API tests')
@allure.title("GET user account detail by email")
def test_api_get_acc_info(api_request):
    response = api_request.get('/api/getUserDetailByEmail', params={'email':'aallee@mail.com'})
    data = response.json()

    assert response.ok
    assert response.status == 200
    assert data['user']['name'] == 'Alexeich'
    assert data['user']['birth_year'] == '2005'

@allure.story('API tests')
@allure.title("DELETE METHOD To Delete User Account")
def test_api_delete_account(api_request):
    payload = {'email':'aallee@mail.com', 'password':'12345678'}
    response = api_request.delete("/api/deleteAccount", form=payload)
    data = response.json()

    assert response.ok
    assert data['responseCode'] == 200
    assert data['message'] == 'Account deleted!'