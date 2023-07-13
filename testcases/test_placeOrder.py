import pytest
from Assignment.pages.landing_page import LandingPage

@pytest.mark.usefixtures("setup")
class TestCases:
    def test_placeOrder(self):
        lp=LandingPage(self.driver)
        loginPage=lp.clickSignUp_Login()
        loginPage.login("test@mailinator.com","12345")