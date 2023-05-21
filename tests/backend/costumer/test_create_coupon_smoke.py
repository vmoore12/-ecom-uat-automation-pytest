import pytest
from ecom_uat_automation_pytest.src.utilities.wooAPIUtility import WooAPIUtility


@pytest.mark.smoke
@pytest.mark.pioneertcid13 
def test_create_27_0ff_coupon_code():
    #  make a call to create a coupon
    woo_helper = WooAPIUtility()

    payload={
        "code": "27off",
        "discount_type": "percent",
        "amount": "25"
    }
    breakpoint()

    rs_body = woo_helper.post("coupons", params=payload, expected_status_code=201)


    #verify coupon code is created

    assert rs_body.status_code == 201,f"Expected status code 201. Actual: {rs_body.status_code}"

    assert rs_body.json['code'] == "25off", f" The wrong  code name was given. Actual: {rs_body.json['code']}"

