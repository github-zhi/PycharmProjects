from test_l.test_LS2_work2.page.index import IndexPage


class TestAddMember:

    def test_add_memeber(self):
        index = IndexPage()

        # index页面->【添加成员】->添加成员信息页面->填写成员信息->【保存】
        # index.goto_add_member().add_member().get_members() # 执行一下，判断框架正确
        # 断言：从get_members->member_list中做断言
        # assert 'xxx' in index.goto_contacts().get_members()

        # 添加成员试一下
        # index.goto_add_member().add_member()

        # 断言
        assert "七一零1" in index.goto_contacts().get_members()


