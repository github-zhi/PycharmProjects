import os
from selenium import webdriver
# 没通，感觉用处不太大，传参有问题
# >browser=firefox pytest test_browser8.py -vs
# 'browser' 不是内部或外部命令，也不是可运行的程序或批处理文件。
class Base():

    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Chrome()

        # 最大化窗口
        self.driver.maximize_window()
        # 隐示等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

class TestBrowser(Base):
    def test_browser(self):
        self.driver.get("https://www.baidu.com")