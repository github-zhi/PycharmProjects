from test_l.test_LS2_work3.page.index import IndexPage


class TestContacts:

    def setup(self):
        self.index = IndexPage()

    def test_add_memeber(self):
        # index = IndexPage() # 放到setup中
        # index页面->【添加成员】->添加成员信息页面->填写成员信息->【保存】
        # index.goto_add_member().add_member().get_members() # 执行一下，判断框架正确
        # 断言：从get_members->member_list中做断言
        # assert 'xxx' in index.goto_contacts().get_members()

        # 添加成员试一下
        self.index.goto_add_member().add_member()


        # 断言
        # assert "七一零1" in index.goto_contacts().get_members()

    # PO原则：同样的行为不同的结果可以建模为不同的方法
    def test_add_member_fail(self):
        self.index.goto_add_member().add_member_fail()

    def test_delete_member(self):
        self.index.goto_contacts().delete_member()

    def test_import_member(self):

        # 首页-通讯录-批量导入/导出-文件导入
        # self.index.goto_contacts().import_member().contacts_import()
        # 首页-导入通讯录
        self.index.goto_import_contact().contacts_import()