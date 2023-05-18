import pytest
from ecom_uat_automation_pytest.src.utilities.genericUtilities import generate_random_email_and_password
from ecom_uat_automation_pytest.src.utilities.wooAPIUtility import WooAPIUtility


@pytest.mark.tcid29
@pytest.mark.pioneertcid11
def test_create_customer_only_email_password():
    # create payload with email and password only
    email_password = generate_random_email_and_password(email_prefix='betest')
    email = email_password['email']
    password = email_password['password']

    print(email_password)
    # make the call 
    woo_helper = WooAPIUtility()
    pay_load = {
        "email": email,
        "password": password
    }

    rs_api = woo_helper.post("customers", params=pay_load, expected_status_code=201)
    # verify response is good

    # verify customers is created by checking the database


    