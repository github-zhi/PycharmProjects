import pytest
import yaml

from homework2_appium.page.app import App


class TestWeWork:

    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.close()

    with open('../datas/data.yaml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        # print(datas)
        addlist = datas['add']
        dellist = datas['del']

    @pytest.mark.parametrize('username, gender, phone', addlist)
    def test_add_contact(self, username, gender, phone):
        toast = self.app.start().main().goto_adress_page().goto_memberinvite().goto_input_add()\
            .edit_username(username).edit_gender(gender).edit_phone(phone).click_save().get_toast()

        assert toast == '添加成功'
        self.app.back()

    @pytest.mark.parametrize('username', dellist)
    def test_del_contact(self, username):
        result = self.app.start().main().goto_adress_page().goto_personal_info(username).goto_personal_info_set()\
            .goto_edit_member().del_member().confirm_del().member_disappear(username)

        assert result == 'True'
