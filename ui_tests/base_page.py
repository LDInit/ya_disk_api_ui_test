from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_url(self):
        return self.driver.get(self.base_url)

    def check_title(self, title):
        return WebDriverWait(self.driver, timeout=3).until(title_is(title))
