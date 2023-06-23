import pytest
from ecom_uat_automation_pytest.automation.src.utilities.wooAPIUtility import WooAPIUtility


@pytest.mark.smoke
@pytest.mark.pioneertcid13 
def test_create_27_0ff_coupon_code():
    #  make a call to create a coupon
    woo_helper = WooAPIUtility()

    payload={
        "code": "24off",
        "discount_type": "percent",
        "amount": "21.00"
    }

    rs_body = woo_helper.post("coupons", params=payload, expected_status_code=201)


    #verify coupon code is created

    assert rs_body['code'] == "24off", f" The wrong  code name was given. Actual: {rs_body['code']}"
    assert rs_body['amount'] =='21.00', f"The wrong amount value was given. Actual: {rs_body['amount']}"

