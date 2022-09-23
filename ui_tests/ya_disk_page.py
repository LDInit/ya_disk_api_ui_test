from base_page import BasePage
from selenium.webdriver.common.by import By


class YaDiskLocators:

    LOCATOR_FILE = (By.CLASS_NAME, "listing-item_type_file")
    LOCATOR_FOLDER = (By.CLASS_NAME, "listing-item_type_dir")
    # able_folders = (By.CLASS_NAME, "b-tree__name")
    LOCATOR_COPY_SUBMIT = (By.CLASS_NAME, "confirmation-dialog__button_submit")
    LOCATOR_FILES_IN_DIR = (By.CLASS_NAME, "listing-item_type_file")
    LOCATOR_FILE_NAME = (By.CLASS_NAME, "listing-item__title")
    LOCATOR_DELETE_BUTTON = (By.XPATH, "//*[@data-key='item-7']")
    LOCATOR_COPY_BUTTON = (By.XPATH, "//*[@data-key='item-5']")
    LOCATOR_EXIST_FOLDERS = (By.CLASS_NAME, "b-tree__name")


class YaDiskHelper(BasePage):

    def __init__(self, driver):
        super(YaDiskHelper, self).__init__(driver)
        self.base_url = "https://disk.yandex.ru/"

    def get_filename(self):
        file = self.find_element(YaDiskLocators.LOCATOR_FILE_NAME)
        name = file.get_attribute("aria-label")
        return name

    def open_context_menu(self):
        file = self.find_element(YaDiskLocators.LOCATOR_FILE)
        return self.action.context_click(file).perform()

    def open_copy_menu(self):
        copy_button = self.find_element(YaDiskLocators.LOCATOR_COPY_BUTTON)
        return copy_button.click()

    def choose_first_folder(self):
        able_folders = self.find_elements(YaDiskLocators.LOCATOR_EXIST_FOLDERS)
        return able_folders[1].click()

    def copy_submit(self):
        copy_submit_button = self.find_element(YaDiskLocators.LOCATOR_COPY_SUBMIT)
        return copy_submit_button.click()

    def open_folder(self):
        folder = self.find_element(YaDiskLocators.LOCATOR_FOLDER)
        return self.action.double_click(folder).perform()

    def delete_extra_files(self, filename):
        files = self.find_elements(YaDiskLocators.LOCATOR_FILES_IN_DIR)
        for file in files:
            name = file.find_element(By.CLASS_NAME, "listing-item__title").get_attribute("aria-label")
            if name != filename:
                self.action.context_click(file).perform()
                delete_button = self.find_element(YaDiskLocators.LOCATOR_DELETE_BUTTON)
                delete_button.click()
        return self.find_elements(YaDiskLocators.LOCATOR_FILES_IN_DIR)