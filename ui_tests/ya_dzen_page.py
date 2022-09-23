from selenium.webdriver import Keys

from base_page import BasePage
from selenium.webdriver.common.by import By


class YaDzenLocators:

    LOCATOR_PROFILE_BUTTON = (By.CLASS_NAME, "dzen-header-desktop__profileMenu-3q")
    LOCATOR_LOGIN_METHOD = (By.XPATH, "//*[@data-type='login']")
    LOCATOR_LOGIN_INPUT = (By.ID, "passp-field-login")
    LOCATOR_PASSWORD_INPUT = (By.ID, "passp-field-passwd")


class YaDzenAuthorizationHelper(BasePage):

    def profile_button_click(self):
        profile_button = self.find_element(YaDzenLocators.LOCATOR_PROFILE_BUTTON)
        return profile_button.click()

    def choose_login_by_email(self):
        login_method_button = self.find_element(YaDzenLocators.LOCATOR_LOGIN_METHOD)
        return login_method_button.click()

    def enter_login(self, login):
        login_input = self.find_element(YaDzenLocators.LOCATOR_LOGIN_INPUT)
        login_input.click()
        return login_input.send_keys(login + Keys.ENTER)

    def enter_password(self, password):
        password_input = self.find_element(YaDzenLocators.LOCATOR_PASSWORD_INPUT)
        password_input.click()
        return password_input.send_keys(password + Keys.ENTER)




