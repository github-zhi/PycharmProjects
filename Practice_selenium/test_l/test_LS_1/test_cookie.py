import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestCookie():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # 打开页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    # 第一次获取cookie时使用
    def test_get_cookie(self):
        time.sleep(15)
        # 一定要在扫码，登录成功之后执行
        cookies = self.driver.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)


    # 使用已存的cookies进行登录，不必每次获取
    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            # 添加一个dict的cookie信息，把cookie键值对，一个一个的塞入浏览器中
            self.driver.add_cookie(cookie)
        # 刷新
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10).\
                until(expected_conditions.element_to_be_clickable((By.ID, "menu_index")))
            if res is not None:
                break

        # # 通过显示等待的方式，等待‘导入通讯录’元素可被点击
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable
        #             ((By.XPATH, "//div[@class='index_service']//a[2]")))
        # self.driver.find_element(By.XPATH, "//div[@class='index_service']//a[2]").click()
        #
        # # 通过显示等待的方式，等待‘上传文件’元素可见
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.presence_of_element_located((By.ID, "js_upload_file_input")))
        #
        # # 上传文件
        # self.driver.find_element(By.XPATH, "//input[@id='js_upload_file_input']").\
        #     send_keys(r"F:\PycharmProjects\Practice_selenium\test_l\test_LS_1\test1.xls")
        #
        # # 通过显示等待的方式，等待‘已上传文件名’元素可见
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.presence_of_element_located((By.ID, "upload_file_name")))
        # # 获取文件名
        # assert_ele = self.driver.find_element(By.ID, "upload_file_name").text
        # print(assert_ele)
        #
        # # 校验文件名
        # assert assert_ele == "test1.xls"
        time.sleep(3000)

