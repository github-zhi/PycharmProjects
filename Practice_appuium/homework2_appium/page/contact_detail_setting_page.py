from appium.webdriver.common.mobileby import MobileBy

from homework2_appium.page.basepage import BasePage
from homework2_appium.page.edit_member_page import EditMember


class ContactDetailSetting(BasePage):
    # 编辑成员
    _edit_member = (MobileBy.XPATH, '//*[@text="编辑成员"]')

    def goto_edit_member(self):
        self.find_and_click(self._edit_member)
        return EditMember(self._driver)