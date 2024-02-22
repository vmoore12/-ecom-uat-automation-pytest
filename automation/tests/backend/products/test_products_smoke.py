
import pytest
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta
from automation.src.dao.product_dao import ProductsDAO
from automation.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from automation.src.utilities.wooAPIUtility import WooAPIUtility
from automation.src.utilities.genericUtilities import generate_random_string, generate_random_float
import logging as logger

pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.products_api]


@pytest.fixture(scope="function")
def create_and_delete_product():
    woo_api_helper = WooAPIUtility()
    # Create a product with regular price
    rand_string = generate_random_string()
    price = generate_random_float()
    
    payload = {
        "name": rand_string,
        "type": "simple",
        "regular_price": price,
    }
    
    rs_api = woo_api_helper.post("products", params=payload, expected_status_code=201)
    
    yield rs_api
    
    # Delete the created product
    if 'id' in rs_api:
        product_id = rs_api['id']
        woo_api_helper.delete(f"products/{product_id}", params={"force": True},expected_status_code=201)




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
def test_update_onsale_price_true(create_and_delete_product):
    product = create_and_delete_product
    woo_api_helper = WooAPIUtility()
    new_prod_id = product['id']
    new_prod_price = product['regular_price']
    new_sale = round(float(new_prod_price) - 2.99,2)
    payload2 = {
        "sale_price": str(new_sale)
    }
    updated_prod = woo_api_helper.put(f"products/{new_prod_id}", params=payload2,expected_status_code=200)
    # verify "on-sale" set to "TRUE" 
    assert updated_prod['on_sale'] == True, f"Updating sale price did not set 'on_sale' to True. It is still set at {updated_prod['on_sale']}."
    assert product['sale_price']== '',f" The sale_price for the created product is already set proir to applying the update filter. It is set at {product['sale_price']}."
    

@pytest.mark.tcid64
def test_set_onsale_price_to_false():
    woo_api_helper = WooAPIUtility()
    prod_doa = ProductsDAO()
    onsale_products = prod_doa.get_random_onsale_product_from_db()
    product_id = onsale_products[0]['product_id']
    payload = {
        "sale_price": " "
    }

    rs_api = woo_api_helper.put(f'products/{product_id}', params= payload, expected_status_code=200)
    assert rs_api['on_sale'] == False,f'The sales price filter did not updated onsale to false. onsale is actually {rs_api["onsale"]}.'

@pytest.mark.tcid65
def test_update_sale_price(create_and_delete_product):
    #create a product
    product = create_and_delete_product
    woo_api_helper = WooAPIUtility()
    new_prod_id = product['id']
    new_prod_price = product['regular_price']
    # Make product on sale
    new_sale = round(float(new_prod_price) - 2.99,2)
    payload = {
        "sale_price": str(new_sale)
    }
    created_prod = woo_api_helper.put(f"products/{new_prod_id}", params=payload, expected_status_code=200)
    assert created_prod['sale_price'] == payload['sale_price'],f"The sale prices are not the same. It should be {payload['sale_price']} but was {created_prod['sale_price']}"

    # Updated sale price
    updated_sale_price = float(new_sale) + .57
    payload2 = {
            "sale_price": str(updated_sale_price)
        }

    rs_api = woo_api_helper.post(f"products/{new_prod_id}", params=payload2, expected_status_code=200)

    # get and update product sale price
    new_prod_id = rs_api['id']
    new_prod_price = rs_api['sale_price']
    #Verify that the sale price was updated
    assert updated_sale_price == float(new_prod_price),f" Updated sale price was not added correctly. It should be {updated_sale_price} not {new_prod_price}."
    assert rs_api['on_sale'] == True,"sale price was not set because 'on_sale' = False."
    assert rs_api['price']>= rs_api['sale_price'],f"Price of the product is not greater than the on sale price which will cause conflict, the price is {rs_api['price']} and the sale price is {rs_api['on_sale']}."