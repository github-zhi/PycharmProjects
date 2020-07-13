from appium.webdriver.webdriver import WebDriver

from app_LS2.test_wechat3.page.basepage import BasePage
from app_LS2.test_wechat3.page.member_invite_page import MemberInvite


class AddressList(BasePage):

    # def __init__(self, driver:WebDriver=None):
    #     self._driver = driver

    # 添加成员
    def add_members(self):
        self._driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("添加成员").instance(0));').click()
        return MemberInvite(self._driver)