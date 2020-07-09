# selenium中如何调用js，当selenium无法实现时，可通过JS实现
# execute_script:执行js
# return:可以返回js的返回结果
# execute_script: arguments传参

# 场景一：js处理-滑动到底部 action6模块中也有该方法
'''def test_touchaction_scrollbottom(self):
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
    sleep(2)'''
from time import sleep

from test_l.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("测试")
        ele_search = self.driver.execute_script("return document.getElementById('su')")
        ele_search.click()

        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_css_selector("#page > div > a.n").click()
        sleep(3)
        # self.driver.execute_script("document.documentElement.scrollTop=10000")
        # self.driver.find_element_by_css_selector("#page > div > a.n").click()
        # sleep(3)

        for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))

    def test_js_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        # 通过JS修改元素属性
        time_ele = self.driver.execute_script("a = document.getElementById('train_date'); a.removeAttribute('readonly')")
        # 通过JS附新值
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(3)