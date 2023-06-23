import pytest
from ecom_uat_automation_pytest.automation.src.pages.HomePage import HomePage
# from  automation.src.selenium_extended import SeleniumExtended

pytestmark = [pytest.mark.feregression, pytest.mark.fesmoke, pytest.mark.HomePage]


@pytest.mark.pioneertcid3
@pytest.mark.usefixtures('init_driver')
@pytest.mark.tcid3
class TestBannerDisplayes:

    

    def test_banner_isdisplayed(self):
        print("Testing If Banner on Homepage is displayed")
        banner_text = 'Free shipping on orders over $50'

        home_page = HomePage(self.driver) # this will open the browser
        home_page.go_to_home_page() # this will go to the homepage
        home_page.get_banner_text() # this gets the banner text
        banner = home_page.get_banner_text()
        assert banner == banner_text, f'This is a match! {banner_text}'
        return banner

    @pytest.mark.tcid4
    def test_verify_home_heading_is_displayed(self):

        header_text = 'Shop'
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()
        home_page.get_shop_heading()
        header = home_page.get_shop_heading().text
        assert header == header_text, f'This is not a match! {header}. Expecting{header_text}.'
        return header

        #NOTE: Why can't i see a return or print a statement here? for example if I do header = home_page.get_shop_heading() \
        # print(header)


        # home_banner = MyAccountSignedOutPage(self.driver)

        # my_acct_page.go_to_my_account()
        # my_acct_page.input_login_username("abcdef@supersqa.com")
        # my_acct_page.input_login_password("abcdefg")
        # my_acct_page.click_login_button()

        # expected_err = "Unknown email address. Check again or try your username."
        # my_acct_page.wait_until_error_is_displayed(expected_err)
