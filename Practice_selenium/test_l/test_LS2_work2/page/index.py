from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_l.test_LS2_work2.page.add_member import AddMember
from test_l.test_LS2_work2.page.contacts import Contacts


class IndexPage:

    # 在work1中实现了框架，下一步就要加入具体的操作了。要先加入driver,元素定位等操作了。
    def __init__(self):
        # 实例化options
        option = Options() # 导入包from selenium.webdriver.chrome.options import Options

        # Google\ Chrome - -remote - debugging - port = 9222
        # 需要和启动命令的端口号一致
        # 指定了一个调试地址
        option.debugger_address = "localhost:9222"
        # 实例变量，加self
        self.driver = webdriver.Chrome(options=option) # 导入包from selenium import webdriver
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(5)

    # 导航栏-通讯录
    def goto_contacts(self):
        self.driver.find_element_by_id("menu_contacts").click()

        return Contacts() # 注意模块的引用

    # 首页-常用入口-添加成员
    def goto_add_member(self):
        # 添加动作
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click() # 导入By包

        return AddMember()

    # 首页-常用入口-导入通讯录
    def goto_import_contact(self):

        return Contacts()

    # 首页-常用入口-成员加入
    def goto_member_join(self):
        pass

    # 首页-常用入口-消息群发
    def goto_create_message(self):
        pass

    # 首页-常用入口-客户联系
    def goto_customer(self):
        pass

    # 首页-常用入口-打卡
    def goto_attendance(self):
        pass