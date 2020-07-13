from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_LS2.test_wechat3.page.basepage import BasePage


class ContactAdd(BasePage):
    # def __init__(self, driver:WebDriver=None):
    #     self._driver = driver

    # 用户名
    def username(self, username="张四"):
        self._driver.find_element_by_xpath(
            "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(username)

        return self

    # 性别
    def gender(self, gender="男"):
        self._driver.find_element_by_xpath("//*[@text='性别']/..//*[@text='男']").click()
        WebDriverWait(self._driver, 10, 0.5).until(
            expected_conditions.visibility_of_element_located(
                (MobileBy.ID, "android:id/content")))
        if gender == '女':
            self._driver.find_element_by_xpath("//*[@text='女']").click()
        else:
            self._driver.find_element_by_xpath("//*[contains(@text, '男')]").click()

        return self

    # 电话
    def phone_num(self, phonenum='19907110000'):
        self._driver.find_element_by_xpath("//*[contains(@text, '手机')]/..//*[@text='手机号']").send_keys(phonenum)

        return self

    def save(self):
        self._driver.find_element_by_xpath("//*[@text='保存']").click()

        from app_LS2.test_wechat3.page.member_invite_page import MemberInvite
        return MemberInvite(self._driver)