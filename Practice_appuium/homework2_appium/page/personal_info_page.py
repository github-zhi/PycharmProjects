from appium.webdriver.common.mobileby import MobileBy

from homework2_appium.page.basepage import BasePage
from homework2_appium.page.contact_detail_setting_page import ContactDetailSetting


class PersonalInfo(BasePage):
    __info_set = (MobileBy.XPATH, '//*[@text="个人信息"]/../../../../..//*[@class="android.widget.RelativeLayout"]')

    # 进入个人信息
    def goto_personal_info_set(self):
        self.find_and_click(self._info_set)
        return ContactDetailSetting(self.driver)