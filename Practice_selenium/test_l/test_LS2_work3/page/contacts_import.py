from selenium.webdriver.common.by import By
from test_l.test_LS2_work3.page.base_page import BasePage
from test_l.test_LS2_work3.page.contacts import Contacts


class Contactsimport(BasePage):

    def contacts_import(self):
        # 通过显示等待的方式，等待‘上传文件’元素可见
        self.wait_until_located(By.ID, "js_upload_file_input")
        # 上传文件
        self.driver.find_element(By.XPATH, "//input[@id='js_upload_file_input']").\
            send_keys(r"F:\PycharmProjects\Practice_selenium\test_l\test_LS2_work3\page\contacts_import_data.xlsx")
        # 导入
        self.find(By.ID, "submit_csv").click()
        # 完成
        self.find(By.ID, "reloadContact").click()

        return Contacts(self.driver)