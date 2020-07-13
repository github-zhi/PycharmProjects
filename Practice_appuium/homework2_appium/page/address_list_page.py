from homework2_appium.page.basepage import BasePage
from homework2_appium.page.member_invite_page import MemberInvite
from homework2_appium.page.personal_info_page import PersonalInfo


class AddressList(BasePage):
    # 添加成员
    def goto_memberinvite(self):
        self.find_by_scroll("添加成员")
        return MemberInvite(self._driver)

    # 个人信息
    def goto_personal_info(self, username):
        self.find_by_scroll(username)
        return PersonalInfo(self._driver)

    def member_disappear(self, username):
        return self.find_and_wait(username)
