import pytest
from src.pages.HomePage import HomePage
from src.selenium_extended import SeleniumExtended


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

  @pytest.mark.tcid106
  def test_product_onsale_is_displayed(self):
    home_page = HomePage(self.driver)
    home_page.go_to_home_page()
    sale_products = home_page.get_onsale_item_text()
    assert sale_products == 'SALE!', f"the products selected does not show that its on sale. It shows {sale_products} instead of 'SALE!'"
