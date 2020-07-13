from appium.webdriver.common.mobileby import MobileBy
from homework2_appium.page.basepage import BasePage
from homework2_appium.page.address_list_page import AddressList


class MainPage(BasePage):
    # 通讯录
    _contact = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dyu"]//*[@text="通讯录"]')

    # 通讯录
    def goto_adress_page(self):
        self.find_and_click(self._contact)
        return AddressList(self._driver)
