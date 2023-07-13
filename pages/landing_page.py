from selenium.webdriver.common.by import By
from Assignment.base.baseDriver import BaseDriver
from Assignment.pages.login_page import LoginPage

class LandingPage(BaseDriver):
    # Locators
    LOGIN_PAGE_FIELD = "//a[normalize-space()='Signup / Login']"

    def __init__(self, driver):
        self.driver = driver
    def getLogin_SignUp_Field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LOGIN_PAGE_FIELD)

    def clickSignUp_Login(self):
        self.getLogin_SignUp_Field().click()
        loginPage = LoginPage(self.driver)
        return loginPage


