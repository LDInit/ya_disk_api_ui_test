import pytest
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session', autouse=False)
def browser():
    options = Options()

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
