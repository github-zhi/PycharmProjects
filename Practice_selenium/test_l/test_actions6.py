# ActionChains:执行PC端的鼠标点击，双击，右键，拖拽等事件
# TouchActions:模拟PC和移动端的点击，滑动，拖拽，多点触控等多种手势操作
# 链式写法

# 用法一：点击、右键、双击操作
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():

    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # 隐示等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    # ActionChains用法一：点击，右键，双击
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        # 注意元素一定要找对
        element_click = self.driver.find_element(By.XPATH, "//input[@value='click me']")
        element_doubleclick = self.driver.find_element(By.XPATH, "//input[@value='dbl click me']")
        element_right = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
        # 分布写法
        action = ActionChains(self.driver)  # 生成一个动作
        action.click(element_click)  # 动作添加
        action.context_click(element_right)
        action.double_click(element_doubleclick)
        action.perform()  # 调用perform()方法执行
        sleep(5)
        # 链式写法
        # ActionChains(self.driver).click(element_click).perform()
        # print("链式写法：执行成功。")

    @pytest.mark.skip
    # ActionChains用法二：移动到某个元素上
    def test_moveto(self):
        self.driver.get("https://www.baidu.com")
        # ele = self.driver.find_element_by_link_text("设置") 定位不到时，换一种定位方式
        ele = self.driver.find_element_by_id("s-usersetting-top")
        # 分布写法
        action = ActionChains(self.driver)  # 生成一个动作
        action.move_to_element(ele)  # 动作添加方法
        action.perform()  # 调用perform()方法执行
        sleep(5)
        # 链式写法
        # ActionChains(self.driver).move_to_element(ele).perform()
        # print("链式写法：执行成功。")

    @pytest.mark.skip
    # ActionChains用法三：拖拽
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element_by_id("dragger")
        drop_ele1 = self.driver.find_element_by_xpath("/html/body/div[2]")
        drop_ele2 = self.driver.find_element_by_xpath("/html/body/div[3]")
        drop_ele3 = self.driver.find_element_by_xpath("/html/body/div[4]")
        drop_ele4 = self.driver.find_element_by_xpath("/html/body/div[5]")
        # 分布写法
        action = ActionChains(self.driver)  # 生成一个动作
        action.drag_and_drop(drag_ele, drop_ele1).perform() # 方法一
        sleep(2)
        action.click_and_hold(drag_ele).release(drop_ele2).perform() # 方法二
        sleep(2)
        action.click_and_hold(drag_ele).move_to_element(drop_ele3).release().perform()  # 方法三
        sleep(2)
        # 链式写法,个人觉得链式写法更好，并且要用drap_and_drop更方便
        ActionChains(self.driver).drag_and_drop(drag_ele, drop_ele4).perform()
        sleep(2)
        print("链式写法：执行成功。")

    @pytest.mark.skip
    # ActionChains用法四：模拟按键
    def test_keys(self):
        self.driver.get("https://www.baidu.com")

        ele = self.driver.find_element_by_id("kw").click()

        action = ActionChains(self.driver)  # 生成一个动作
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()

class TestTouchAction():

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        # 隐示等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    # 需要加option，并且chrome可以，firefox不行
    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")

        ele.send_keys("测试")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()

        action.scroll_from_element(ele, 0, 10000).perform()
        sleep(2)
        # 下一页
        self.driver.find_element_by_css_selector("#page > div > a.n").click()
        action.scroll_from_element(ele, 0, 10000).perform()
        sleep(2)

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sing_in")
        sleep(3)
        self.driver.find_element_by_id("user_login").send_keys("user")
        self.driver.find_element_by_id("user_password").send_keys("password")
        self.driver.find_element_by_id("user_remember_me").click()


# 亦可以使用python解释器来执行
# if __name__ == '__main__':
#     pytest.main(['-v', '-s', 'test_actions6.py'])