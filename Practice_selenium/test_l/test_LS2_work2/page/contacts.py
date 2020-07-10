from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Contacts:

    def __init__(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)

    def get_members(self):
        # 获取通讯列表
        elements = self.driver.find_elements(By.CSS_SELECTOR,
                      ".member_colRight_memberTable_tr .member_colRight_memberTable_td:nth-child(2)")
        # 姓名列表
        name_list = [element.get_attribute("title") for element in elements]
        # print(name_list)

        return name_list
