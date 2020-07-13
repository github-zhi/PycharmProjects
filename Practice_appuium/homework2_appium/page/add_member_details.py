from appium.webdriver.common.mobileby import MobileBy
from homework2_appium.page.basepage import BasePage

class ContactAdd(BasePage):
    # 姓名
    _username = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b5t"]/*[@text="必填"]')
    # 性别
    _gender = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/csp"]//*[@text="男"]')
    _gender_male = (MobileBy.XPATH, '//*[@text="男"]')
    _gender_female = (MobileBy.XPATH, '//*[@text="女"]')
    # 手机号
    _phone = (MobileBy.XPATH, '//*[@text="手机号"]')
    # 保存
    _save = (MobileBy.XPATH, '//*[@text="保存"]')

    def edit_username(self, username):
        self.find_and_sendkeys(self._username, f"{username}")
        return self

    def edit_gender(self, gender):
        self.find_and_click(self._gender)
        if gender == '男':
            self.find_and_click(self._gender_male)
        else:
            self.find_and_click(self._gender_female)
        return self

    def edit_phone(self, phone):
        self.find_and_sendkeys(self._phone, f"{phone}")
        return self

    def click_save(self):
        self.find_and_click(self._save)

        from homework2_appium.page.member_invite_page import MemberInvite
        return MemberInvite(self._driver)


