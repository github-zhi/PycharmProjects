import pytest
import allure

@allure.feature("登录")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("测试：登录成功")
        pass

    @allure.story("登录失败")
    def test_login_fail(self):
        print("测试：登录失败。")
        pass

    @allure.story("用户名缺失")
    def test_login_username(self):
        print("无用户名")
        pass

    @allure.story("密码缺失")
    @allure.link("www.baidu.com",name="这是链接")# 应该是测试地址，做备注，如果出问题了在报告中体现，便于找问题
    # 把所执行的测试用例标记上
    Test_Case_link = "www.jira.com"
    @allure.testcase(Test_case_link, "登录用例")
    # bug产生后提交
    # --allure-link-pattern=issue:http://www.jira.com/issue/{}
    @allure.issue('1001', '这是一个issue')
    def test_loign_password(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("密码输入")
        with allure.step("点击登录之后登录失败"):
            assert 1 == 2
            print("登录失败")