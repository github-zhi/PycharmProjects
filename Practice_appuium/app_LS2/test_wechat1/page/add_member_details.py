

class ContactAdd:
    # 用户名
    def username(self):
        return self

    # 性别
    def gender(self):
        return self

    # 电话
    def phone_num(self):
        return self

    def save(self):
        from app_LS2.test_wechat1.page.member_invite_page import MemberInvite
        return MemberInvite()