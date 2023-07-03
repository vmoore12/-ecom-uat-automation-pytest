import pytest
from ecom_uat_automation_pytest.automation.src.pages.HomePage import HomePage
# from src.selenium_extended import SeleniumExtended

pytestmark = [pytest.mark.feregression, pytest.mark.fesmoke, pytest.mark.HomePage]




@pytest.mark.usefixtures('init_driver')

class TestHomePage:
  # go to home page
  #find all products on page
  # loop through products and verify that product name is a string.
  @pytest.mark.tcid5
  def test_product_name_as_string(self):
    home_page = HomePage(self.driver)
    home_page.go_to_home_page()
    product_name = home_page.get_all_products_name()
    for i in product_name:
      names = i.text
    print(len(names))
    assert isinstance(names, str), f'this not a string. It is {type(names)}.'

  @pytest.mark.tcid6 
  def test_header_menu_is_displayed(self):

    # go to home page
    home_page = HomePage(self.driver)
    home_page.go_to_home_page()
    # find the header menu element
    header_menu = home_page.get_header_menu()
    header_titles = header_menu.text.split('\n')
    print(header_titles)
    # verify that the header menu is displayed
    menu_list = ['Home', 'Cart','Checkout', 'My account', 'Sample Page'] # NOTE: got to figure out how to make this dynamic!
    for header_titles, menu_list in zip(header_titles, menu_list):
      assert header_titles == menu_list, f'{header_menu} and {menu_list} did not match.'




    
