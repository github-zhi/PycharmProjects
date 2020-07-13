
from app_LS2.test_wechat3.page.address_list_page import AddressList
from app_LS2.test_wechat3.page.basepage import BasePage


class MainPape(BasePage):
    # def __init__(self, driver:WebDriver=None):
    #     self._driver = driver

    #  通讯录 Address
    def goto_adress_page(self):
        return AddressList(self._driver)

    def goto_message(self):
        pass

    def goto_workbench(self):
        pass