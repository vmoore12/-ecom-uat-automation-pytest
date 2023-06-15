import pytest
from  automation.src.pages.HomePage import HomePage
# from src.selenium_extended import SeleniumExtended

pytestmark = [pytest.mark.feregression, pytest.mark.fesmoke, pytest.mark.HomePage]




@pytest.mark.usefixtures('init_driver')
@pytest.mark.tcid5
class TestProductName:
  # go to home page
  #find all products on page
  # loop through products and verify that product name is a string.
  def test_product_name_as_string(self):
    home_page = HomePage(self.driver)
    home_page.go_to_home_page()
    product_name = home_page.get_all_products_name()
    for i in product_name:
      names = i.text
    print(len(names))
    assert isinstance(names, str), f'this not a string. It is {type(names)}.'
