from selenium.webdriver.common.by import By
from test_l.test_PageObject.Page.base_page import BasePage
from test_l.test_PageObject.Page.register import Register


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)