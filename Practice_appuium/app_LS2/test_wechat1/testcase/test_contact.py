from app_LS2.test_wechat1.page.app import App


class TestWeWork:
    def setup(self):
        self.app = App()

    def test_contact(self):
        self.app.start().goto_mainpage().goto_adress_page().add_members().manual_input_add(). \
            username().gender().phone_num().save().get_result()
        toast = self.app.start().goto_mainpage().goto_adress_page().add_members().manual_input_add().\
            username().gender().phone_num().save().get_result()

        assert '添加成功' == toast