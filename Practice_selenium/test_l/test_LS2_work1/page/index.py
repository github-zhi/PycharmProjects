from test_l.test_LS2_work1.page.add_member import AddMember
from test_l.test_LS2_work1.page.contacts import Contacts


class IndexPage:

    # 导航栏-通讯录
    def goto_ontacts(self):

        return Contacts() # 注意模块的引用

    # 首页-常用入口-添加成员
    def goto_add_member(self):

        return AddMember()

    # 首页-常用入口-导入通讯录
    def goto_import_contact(self):

        return Contacts()

    # 首页-常用入口-成员加入
    def goto_member_join(self):
        pass

    # 首页-常用入口-消息群发
    def goto_create_message(self):
        pass

    # 首页-常用入口-客户联系
    def goto_customer(self):
        pass

    # 首页-常用入口-打卡
    def goto_attendance(self):
        pass