from test_l.test_PageObject.Page.main import Main


class TestRegister:
    def setup(self):
        # 声明main函数，实例化
        self.main = Main()

    def test_register(self):
        # 链式调用所需要的方法
        # 首页》立即注册》填写注册信息
        assert self.main.goto_register().register()
        # 首页》企业登录》企业注册》填写注册信息
        # assert self.main.goto_login().goto_register().register()
