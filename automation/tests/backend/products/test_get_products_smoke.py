
import pytest
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta
from ecom_uat_automation_pytest.automation.src.dao.product_dao import ProductsDAO
from ecom_uat_automation_pytest.automation.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ecom_uat_automation_pytest.automation.src.utilities.wooAPIUtility import WooAPIUtility
from ecom_uat_automation_pytest.automation.src.utilities.genericUtilities import generate_random_string, generate_random_float
import logging as logger

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.products_api]


@pytest.mark.tcid24
@pytest.mark.pioneertcid15
def test_get_all_products_returns_not_empty():
    woo_api_helper = WooAPIUtility()
    rs_api = woo_api_helper.get("products", expected_status_code=200)
    assert rs_api, "Get all products endpoint returned nothing."

@pytest.mark.tcid25
@pytest.mark.pioneertcid14
def test_get_product_by_id():

    # get product that exists from db (also could have gotten it from api (list-products))
    product_dao = ProductsDAO()
    rand_product = product_dao.get_random_product_from_db()
    product_id = rand_product[0]['ID']
    product_name = rand_product[0]['post_name']
    product_title = rand_product[0]['post_title']
    logger.info(f"Test product id: {product_id}")

    # make the api call
    product_helper = ProductsAPIHelper()
    rs_api = product_helper.call_get_product_py_id(product_id)

    assert rs_api['id'] == product_id, f"Get product call. Id in request does not match id in response."
    assert rs_api['slug'] == product_name, f'name mismatch'
    assert rs_api['name'] == product_title, f'title mismatch'



@pytest.mark.tcid26
@pytest.mark.pioneertcid19
def test_create_simple_product():
    #create product payload
    woo_api_helper = WooAPIUtility()
    rand_string = generate_random_string()
    price = generate_random_float()

    payload = {
        "name": rand_string,
        "type":"simple",
        "regular_price":price,
    }

    rs_api = woo_api_helper.post("products", params=payload,expected_status_code=201)
    assert rs_api['slug'] == payload['name'],f"Product name was entered incorrectly. It should be {payload['name']} but was {rs_api['slug']}."
    assert rs_api['regular_price'] == payload['regular_price'],f"Regular price was entered incorrectly. It should be {payload['regular_price']}."
    assert rs_api['type'] == "simple",f"Product type was entered incorrectly. It should be {payload['type']} but is {rs_api['type']}."
    logger.info(f"Test product name: {rs_api}")


@pytest.mark.tcid51
def test_list_products_with_after_filter():
    woo_api_helper = WooAPIUtility()
    # get current date
    current_date = datetime.now()

    # subtract 1 month from current date
    new_date = str(current_date - relativedelta(months=1))
    payload = {
        "after": new_date,
        "per_page":"100"
    }

    rs_api = woo_api_helper.get("products", params=payload)
    data = []
    for i in rs_api:
        data.append(i['date_created'].strip(''))
    for date in data: 
        assert date >=payload['after'],f"The date created dose not fall into the 'after' filter range. It should be equal to or after {payload['after']}, but result was {date}."



@pytest.mark.tcid61
def test_update_regular_price():
    # Database helper object:
    woo_api_helper = WooAPIUtility()
    # get random product from db
    prod_doa = ProductsDAO()
    rand_product = prod_doa.get_random_product_from_db()
    # extract the random 
    product_id = rand_product[0]['ID']
    updated_price = str(random.randint(10, 100)) + '.' + str(random.randint(10, 99))
    payload = {
        "regular_price": updated_price
    }
    rs_api = woo_api_helper.put(f"products/{product_id}", params=payload,expected_status_code=200)

    assert rs_api['regular_price'] == payload['regular_price'], F'The regular price filter did not update the regular price given to the payload.'

@pytest.mark.tcid63
def test_update_sales_price():
    woo_api_helper = WooAPIUtility()
    prod_doa = ProductsDAO()
    rand_products = prod_doa.get_random_product_from_db()
    product_id = rand_products[0]['ID']
    updated_price = str(random.randint(1, 20)) + '.' + str(random.randint(10, 99))
    payload = {
        "sale_price": updated_price
    }
    
    rs_api = woo_api_helper.put(f"products/{product_id}", params= payload)

    assert rs_api['on_sale'] == True,f'The sales price filter did not update on_sale given to the payload. '
    # assert updated_price < rs_api['price'], f'The onsale price is more than the regular price. On_sale price is set to {rs_api["on_sale"]} and the regular price is {rs_api["price"]}.'


@pytest.mark.tcid64
def test_set_onsale_price_to_false():
    woo_api_helper = WooAPIUtility()
    prod_doa = ProductsDAO()
    onsale_products = prod_doa.get_random_onsale_product_from_db()
    product_id = onsale_products[0]['product_id']
    payload = {
        "sale_price": " "
    }

    rs_api = woo_api_helper.put(f'products/{product_id}', params= payload)
    assert rs_api['on_sale'] == False,f'The sales price filter did not updated onsale to false. onsale is actually {rs_api["onsale"]}.'

