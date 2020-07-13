from appium.webdriver.common.mobileby import MobileBy
from homework2_appium.page.basepage import BasePage


class EditMember(BasePage):
    # 删除
    _del_member = (MobileBy.XPATH, '//*[@text="删除成员"]')
    # 确定
    _confirm_del = (MobileBy.XPATH, '//*[@text="确定"]')
    # 取消
    _cancel_del = (MobileBy.XPATH, '//*[@text="取消"]')

    def del_member(self):
        self.find_and_click(self._del_member)
        return self

    def confirm_del(self):
        self.find_and_click(self._confirm_del)

        from homework2_appium.page.address_list_page import AddressList
        return AddressList(self._driver)

    def cancel_del(self):
        self.find_and_click(self. _cancel_del)
        return self
