
import pytest
from ecom_uat_automation_pytest.src.dao.product_dao import ProductsDAO
from ecom_uat_automation_pytest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ecom_uat_automation_pytest.src.utilities.wooAPIUtility import WooAPIUtility
from ecom_uat_automation_pytest.src.utilities.genericUtilities import generate_random_string, generate_random_float
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



@pytest.mark.tcid31
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
    breakpoint()
    assert rs_api['slug'] == payload['name'],f"Product name was entered incorrectly. It should be {payload['name']} but was {rs_api['slug']}."
    assert rs_api['regular_price'] == payload['regular_price'],f"Regular price was entered incorrectly. It should be {payload['regular_price']}."
    assert rs_api['type'] == "simple",f"Product type was entered incorrectly. It should be {payload['type']} but is {rs_api['type']}."
    logger.info(f"Test product name: {rs_api}")




