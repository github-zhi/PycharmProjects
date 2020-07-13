from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import assert_that, close_to
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW():
    def setup(self):
        caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",
            "unicodeKeyBoard": "true", # 是否需要输入非英文之外的语言
            "resetKeyBoard": "true", # 在测试完成后重置输入法
            "noReset": "true", # 是否在测试前后重置相关环境（如首次打开弹框或登录信息）fullReset
            # "dontStopAppOnReset": "true", # 首次启动时，不停止app（可调试或运行时提升运行速度
            "skipDeviceInitialization": "true" # 跳过安装、权限设置等操作（可调试或运行时提升运行速度
        }
        # 创建驱动，初始化driver
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()
        # 关闭这个session
        # self.driver.quit()
        pass

    def test_search(self):
        '''
        1.打开app
        2.点击搜索输入框
        3.搜索框输入“阿里巴巴" or “小米”
        4.在搜索结果里选择 阿里巴巴 ，点击
        5.判断股价格
        :return:
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        # 显式等待
        element = WebDriverWait(self.driver, 10, 0.5).until\
            (expected_conditions.element_to_be_clickable(
                (MobileBy.ID, "com.xueqiu.android:id/search_input_text"))) # 注意（）
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        sleep(2)
        # 可以使用组合定位
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        expect_price = 250
        # assert current_price >200
        assert_that(current_price, close_to(expect_price, expect_price*0.1))

    @pytest.mark.parametrize('sendkey, type, expect_price',[
        ('阿里巴巴', 'BABA', 250),
        ('xiaomi', '01810', 30)
    ])
    def test_search_param(self, sendkey, type, expect_price):

        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        # 显式等待
        element = WebDriverWait(self.driver, 10, 0.5).until\
            (expected_conditions.element_to_be_clickable(
                (MobileBy.ID, "com.xueqiu.android:id/search_input_text"))) # 注意（）
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(sendkey)
        sleep(2)
        # 可以使用组合定位
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        current_price = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{type}'/../../..//*@resource-id='com.xueqiu.android:id/current_price']")

        assert_that(current_price, close_to(expect_price, expect_price*0.1))