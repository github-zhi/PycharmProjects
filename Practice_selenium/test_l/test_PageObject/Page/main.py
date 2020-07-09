from selenium.webdriver.common.by import By
from test_l.test_PageObject.Page.base_page import BasePage
from test_l.test_PageObject.Page.login import Login
from test_l.test_PageObject.Page.register import Register

# 继承BasePage类，使用其中的方法
class Main(BasePage):
    # 先声明访问地址，以传给base_page中的_base_url
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        # 使用BasePage中封装的find方法，定位'立即注册'元素
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        # 返回到注册页面，但注册页面还没建，去建Register模块
        return Register(self._driver)
        # 写完Register，需要导入引用；并且要传入driver

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)
