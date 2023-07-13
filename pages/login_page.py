from selenium.webdriver.common.by import By
from Assignment.base.baseDriver import BaseDriver

class LoginPage(BaseDriver):
    #locators
    EMAIL_FIELD = "//input[@data-qa='login-email']"
    PASSWORD_FIELD = "//input[@placeholder='Password']"
    LOGIN_BUTTON = "//button[normalize-space()='Login']"

    def __init__(self,driver):
        self.driver=driver

    def getEmailField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EMAIL_FIELD)

    def getPasswordField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PASSWORD_FIELD)

    def getLoginField(self):
        return self.wait_until_element_is_clickable(By.XPATH, "//button[normalize-space()='Login']")
    def fillUsername(self, email):
        self.getEmailField().send_keys(email)

    def fillPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLogin(self):
        self.getLoginField().click()

    def login(self, username, password):
        self.fillUsername(username)
        self.fillPassword(password)
        self.clickLogin()
