from selenium.webdriver.common.by import By
from test_l.test_LS2_work3.page.base_page import BasePage


class Contacts(BasePage):

    # 获取通讯录列表
    def get_members(self):
        elements = self.finds(By.CSS_SELECTOR,
                      ".member_colRight_memberTable_tr .member_colRight_memberTable_td:nth-child(2)")
        # 姓名列表
        name_list = [element.get_attribute("title") for element in elements]
        # print(name_list)

        return name_list

    def import_member(self):
        pass
        # ele_import = self.find\
        #     (By.XPATH, "//*[@id='js_contacts1368']/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/a/div[1]")
        # self.wait_until_clickable(ele_import)
        # ele_import.click()
        #
        # ele_import_file = self.find\
        #     (By.XPATH, "//*[@id='js_contacts1060']/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/ul/li[1]/a")
        # ele_import_file.click()
        #
        # return Contacts_import(self.driver)

    def delete_member(self):
        # 选择要删除人员的复选框
        self.find(By.CSS_SELECTOR, '#member_list tr:nth-child(3) input').click()
        self.find(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_delete').click()
        # 删除div弹框,确定删除
        self.wait_until_clickable(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]")
        self.find(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()

