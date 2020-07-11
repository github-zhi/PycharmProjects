from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_l.test_LS2_work2.page.contacts import Contacts


class AddMember:
    # OP原则：不要暴露页面内部的元素给外部
    # 定义类变量
    # username = "username" # 在其它地方调用时index.goto_add_member().会显示出username这个变量
    _username = "username" # 加下划线开头，就不会出现上面问题,此时下面的变量要使用self._username

    def __init__(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)

    def add_member(self):
        # 填写添加成员信息
        self.driver.find_element(By.ID, self._username).send_keys("七一零4")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("071004")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("19907100004")

        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

        return Contacts()

    def add_member_fail(self):
        # 添加失败
        self.driver.find_element(By.ID, self._username).send_keys("七一零1")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("071001")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("19907100001")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return Contacts()