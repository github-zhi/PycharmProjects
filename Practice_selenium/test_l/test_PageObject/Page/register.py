from selenium.webdriver.common.by import By
from test_l.test_PageObject.Page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("企业名")
        self.find(By.ID, "manager_name").send_keys("管理员")
        self.find(By.ID, "register_tel").send_keys("19907060000")
        return True
