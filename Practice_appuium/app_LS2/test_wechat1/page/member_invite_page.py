


class MemberInvite:
    # 手动输入添加
    def manual_input_add(self):
        from app_LS2.test_wechat1.page.add_member_details import ContactAdd
        return ContactAdd()

    def get_result(self):
        return "添加成功"