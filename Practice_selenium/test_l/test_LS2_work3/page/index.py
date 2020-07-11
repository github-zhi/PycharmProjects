from selenium.webdriver.common.by import By

from test_l.test_LS2_work3.page.add_member import AddMember
from test_l.test_LS2_work3.page.base_page import BasePage
from test_l.test_LS2_work3.page.contacts import Contacts
from test_l.test_LS2_work3.page.contacts_import import Contactsimport


class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 导航栏-通讯录//*[@id="menu_contacts"]/span
    def goto_contacts(self):
        self.find(By.ID, "menu_contacts").click()
        return Contacts(self.driver) # 注意模块的引用

    # 首页-常用入口-添加成员
    def goto_add_member(self):
        # 添加动作
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click() # 导入By包
        return AddMember(self.driver)

    # 首页-常用入口-添加成员
    def goto_import_contact(self):
        self.find(By.XPATH, "//div[@class='index_service']//a[2]").click()
        return Contactsimport(self.driver)