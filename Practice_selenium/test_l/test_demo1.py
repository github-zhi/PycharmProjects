from selenium import webdriver


class TestDemo1():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys("时间")
        self.driver.find_element_by_id("su").click()
