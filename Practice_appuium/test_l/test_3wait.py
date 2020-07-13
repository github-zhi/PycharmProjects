from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
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
        # 关闭这个session
        self.driver.quit()

    def test_search(self):
        '''
        1.打开app
        2.点击搜索输入框
        3.搜索框输入“阿里巴巴"
        4.在搜索结果里选择 阿里巴巴 ，点击
        5.获取股价，判断价格>200
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
        assert current_price >200

    def test_assert(self):
        '''
        打开‘雪球’应用首页
        定位首页的搜索框
        判断搜索框是否可用，并查看搜索框name属性
        打印搜索框
        输入“阿里巴巴”
        判断【阿里巴巴】是否可见
        如果可见，打印“搜索成功”，如果不可见，打印“搜索失败”
        :return:
        '''
        ele = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        # print(ele.is_enabled())
        print(ele.text)
        print(ele.location)
        print(ele.size)

        search_enable = ele.is_enabled()
        if search_enable == True:
            ele.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            ele_ali = self.driver.find_element_by_xpath\
                ("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # ele_ali.is_displayed()
            print(ele_ali.get_attribute("displayed"))
            ele_display = ele_ali.get_attribute("displayed")
            if ele_display == 'true':
                print("成功")
            else:
                print("失败")

    def test_touchaction(self):
        # TouchAction().press(el0).moveTo(el1).release()
        action = TouchAction(self.driver)

        # 不建议写坐标，一改变都要维护
        # action.press(x=400, y=1300).wait(3000).move_to(x=400, y=150).release().perform()
        # action.press(x=400, y=1300).wait(3000).move_to(x=400, y=150).release().perform()

        # 改变屏幕尺寸后照常可用
        window_rect = self.driver.get_window_rect()
        # print(window_rect)
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 9 / 10)
        y_end = int(height * 1 / 10)
        action.press(x=x1, y=y_start).wait(3000).move_to(x=x1, y=y_end).release().perform()
        action.press(x=x1, y=y_start).wait(3000).move_to(x=x1, y=y_end).release().perform()

    @pytest.mark.skip
    # 开锁手势
    def test_touchaction_unlock(self):
        action = TouchAction(self.driver)
        # 尽量用元素，取不到元素，再用坐标点
        action.press(x=x1, y=y1).wait(100).move_to(x=x2, y=y2).wait(100).move_to(x=x3, y=y3).wait(100) \
            .move_to(x=x4, y=y4).wait(100).move_to(x=x5, y=y5).wait(100).move_to(x=x6, y=y6).wait(100) \
            .release().perform()

if __name__ == '__main__':
    pytest.main()

