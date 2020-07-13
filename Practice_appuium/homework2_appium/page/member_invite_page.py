from appium.webdriver.common.mobileby import MobileBy
from homework2_appium.page.basepage import BasePage


class MemberInvite(BasePage):
    _ele_add = (MobileBy.XPATH, '//*[@text="手动输入添加"]')

    # 手动输入添加
    def goto_input_add(self):
        self.find_and_click(self._ele_add)

        from homework2_appium.page.add_member_details import ContactAdd
        return ContactAdd(self._driver)

    def get_toast(self):
        toast = self._driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
        return toast
