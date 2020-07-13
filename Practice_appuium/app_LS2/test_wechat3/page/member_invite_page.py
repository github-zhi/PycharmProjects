
from appium.webdriver.webdriver import WebDriver

from app_LS2.test_wechat3.page.basepage import BasePage


class MemberInvite(BasePage):
    # def __init__(self, driver:WebDriver=None):
    #     self._driver = driver

    # 手动输入添加
    def manual_input_add(self):
        self._driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        from app_LS2.test_wechat3.page.add_member_details import ContactAdd
        return ContactAdd(self._driver)

    def get_result(self):
        return "添加成功"