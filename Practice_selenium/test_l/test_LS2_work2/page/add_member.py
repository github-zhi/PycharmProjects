from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_l.test_LS2_work2.page.contacts import Contacts


class AddMember:

    def __init__(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)

    def add_member(self):
        # 填写添加成员信息
        self.driver.find_element(By.ID, "username").send_keys("七一零1")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("071001")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("19907100001")

        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

        return Contacts()

