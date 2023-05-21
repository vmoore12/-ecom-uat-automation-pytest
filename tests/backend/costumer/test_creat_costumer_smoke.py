import logging as logger
import pytest
import os
from ecom_uat_automation_pytest.src.utilities.genericUtilities import generate_random_email_and_password
from ecom_uat_automation_pytest.src.utilities.wooAPIUtility import WooAPIUtility
from ecom_uat_automation_pytest.src.dao.customers_dao import CustomersDAO



pytestmark = [pytest.mark.beregression, pytest.mark.smoke,pytest.mark.customers_api,] # when we have multiple test cases that are the sme type so we want to run he same marks so we mark them like this. 

@pytest.mark.tcid29
@pytest.mark.pioneertcid11
def test_create_customer_only_email_password():
    # create payload with email and password only
    email_password = generate_random_email_and_password(email_prefix='betest')
    email = email_password['email']
    password = email_password['password']
    breakpoint()

    print(email_password)
    # make the call 
    woo_helper = WooAPIUtility()
    payload = {
        "email": email,
        "password": password
    }
    rs_body = woo_helper.post("customers", params=payload, expected_status_code=201)

    # verify response is good
    assert rs_body, f'Response of create customers call should not be empty.'

    assert rs_body['id'], f'ID should be presented in response.'
    assert isinstance(rs_body['id'], int), f'The id in response of create custome should be numeric.'
    assert email == rs_body['email'], f'Create customer endpoint email in response does not match in request.'\
        f"Expected {email}, Actual:{rs_body['email']}"
    assert rs_body['role'] == 'customer', f"Create new customer API, customer role should be 'customer' but it was '{rs_body['role']}'"

    # verify customers is created by checking the database
    customer_helper = CustomersDAO()
    db_info = customer_helper.get_customer_by_email(email)
    assert len(db_info) == 1, f"Expected 1 record for customer in'users' table. But found {len(db_info)}" 
    assert db_info[0]['user_pass'], f"After creating user with api, the password field in DB is empty."

    expected_display_name = email.split('@')[0] 

    assert db_info[0]['display_name'] == expected_display_name, f"Display name database does not match expected." \
                                                                f"Email: {email} Expected display:{expected_display_name}," f"DB display name: {db_info[0]['display_name']}"
    assert db_info[0]['display_name'] == expected_display_name, f"Display name database does not match expected." \
                                                                f"Email: {email} Expected display:{expected_display_name}" f"DB display name: {db_info[0]['user_login']}"
    

@pytest.mark.tcid47
@pytest.mark.pioneertcid12
def test_create_customer_fail_for_existing_email():
    
    # get random existing customer(from api or db) - in this example we get from the db
    cust_dao = CustomersDAO() # imported the class and put it in a variable (cust_dao)
    rand_cust = cust_dao.get_random_customer_from_db() # used the function from the class we need and set in a variable(rand_cust). If its not there then w have to create a new function to do what we need.
    # breakpoint()
    rand_email = rand_cust[0]['user_email'] # since rand_cust is a list with 1 dict inside  we get the first dict in the list[0], and the "value" 'user_email' of the dict.
    logger.debug(f'Random email for the test: {rand_email}')


  
    # call api to create customer with the existing user
    email_password = generate_random_email_and_password(email_prefix="pioneertcid11")
    random_password =  email_password['password']
    woo_helper = WooAPIUtility()
    payload = {
        "email": rand_email,
        "password": random_password
    }
    rs_body = woo_helper.post("customers", params=payload, expected_status_code=400)
    breakpoint()


    # verify the api response is a failure 
    #     #option 1:
    # if rs_body['code'] != 'registration-error-email-exists':
    #     raise Exception()

    # option 2:
    assert rs_body['code'] =='registration-error-email-exists',f"Create customer with existing user response does not" \
                                 f"have expected text. Expected: 'registration-error-email-exists', Actual: {rs_body['code']}"
    assert rs_body['data']['status'] == 400, f"Unexpected status code in body of response. " \
                    f"Expected: 400, Actual: {rs_body['data']['status']}"
    
    
    assert 'An account is already registered with your email address.' in rs_body['message'], f"Create customer with " \
                                    f"existing user. Response body 'message' did not contain expected text."
