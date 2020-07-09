# 注意代码里所要引用的包
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 直接等待 time.sleep(3)
# 隐示等待 self.driver.implicitly_wait(5) 是全局性的。设置一个等待时间，轮查查找（默认0.5s）元素是否出现，如果超时未出现抛出异常。
# 显示等待：在代码中定义等待条件，当条件发生时才继续执行代码。WebDriverWait配合until()和until_not()方法，根据判断条件进行等待。
# 程序每隔一段时间（默认0.5秒）进行条件判断，条件成立，则执行下一步，否则继续等待，直到超时设置的最长时间

class TestWait():

    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # 隐示等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://testerhome.com/")
        # 强制等待
        sleep(3)
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        # 显示等待
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@class="active"]')) >= 1
        WebDriverWait(self.driver, 10).until(wait) # 注意不要加()，加上就相当于调用了。
        # 上面成功等待到指定元素后，才执行后面的
        self.driver.find_element(By.XPATH, '//*[@class="team-name"]').click()
        print("成功")

    # 显示等待WebDriverWait expected_conditions
    def test_wait_expected(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        WebDriverWait(self.driver, 10).until\
            (expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="team-name"]')))
        self.driver.find_element_by_link_text("社团").click()
        print("成功！")