from ya_dzen_page import YaDzenAuthorizationHelper
from ya_disk_page import YaDiskHelper


LOGIN = "makeitbettersoon@yandex.ru"
PASS = "LetsdoIT123"
FILE_TO_COPY = "Файл для копирования.jpg"


class TestClass:

    def test_ya_disk_copy_file(self, browser):
        """
        end-o-end test:
        1. login Yandex
        2. go to Yandex Disk
        3. copy existing file to the existing subfolder
        4. go to the subfolder
        5. remove all files except of the copied file
        """
        ya_dzen_page = YaDzenAuthorizationHelper(browser)
        ya_dzen_page.go_to_url()
        ya_dzen_page.profile_button_click()
        ya_dzen_page.choose_login_by_email()
        ya_dzen_page.enter_login(LOGIN)
        ya_dzen_page.enter_password(PASS)

        assert ya_dzen_page.check_title("Дзен")

        ya_disk_page = YaDiskHelper(browser)
        ya_disk_page.go_to_url()
        ya_disk_page.open_context_menu()
        ya_disk_page.open_copy_menu()
        ya_disk_page.choose_first_folder()
        ya_disk_page.copy_submit()
        ya_disk_page.open_folder()
        files = ya_disk_page.delete_extra_files(FILE_TO_COPY)

        assert len(files) == 1
        assert ya_disk_page.get_filename() == FILE_TO_COPY




