from time import sleep

import pytest
import yaml
from appium import webdriver

class TestWechat:
    def setup(self):
        caps = {"deviceName": "127.0.0.1:7555",
                "platformName": "Android",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": "true"}
        # 创建驱动
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 关闭这个session
        self.driver.quit()

    def test_add_contact(self):
        # 要添加的人员信息
        username = "李一女"
        gender = '女'
        phonenum = '19907130001'

        # 2、点击通讯录
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        sleep(3)

        # 3、滚动找到添加成员，点击添加成员
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("添加成员").instance(0));').click()

        # 4、选择手动添加成员
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()

        # 5、输入姓名，性别，手机号，点击保存按钮
        # 输入姓名
        self.driver.find_element_by_xpath(
            "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(username)
        # 设置性别
        self.driver.find_element_by_xpath("//*[@text='性别']/..//*[@text='男']").click()
        sleep(2)
        if gender == '女':
            self.driver.find_element_by_xpath("//*[@text='女']").click()
        else:
            self.driver.find_element_by_xpath("//*[contains(@text, '男')]").click()
        # 手机号
        self.driver.find_element_by_xpath("//*[contains(@text, '手机')]/..//*[@text='手机号']").send_keys(phonenum)
        # 点击【保存】
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        # 验证‘添加成功’信息
        toasttext = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert toasttext == '添加成功'

    @pytest.mark.skip
    def test_del_contact(self):
        # 1、要删除人员的姓名
        username = "张菲"
        # 2、点击通讯录
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        # 3、找到要删除的人员
        self.driver.find_element_by_xpath(f"//* [@text='{username}']").click()
        # 4、进入个人信息
        self.driver.find_element_by_xpath(
            '//*[@text="个人信息"]/../../../../..//*[@class="android.widget.RelativeLayout"]').click()
        # 5、编辑成员
        self.driver.find_element_by_xpath('//*[@text="编辑成员"]').click()
        # 6、删除成员
        self.driver.find_element_by_xpath('//*[@text="删除成员"]').click()
        # 7、确定删除
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        # 8、验证已删除人员不在列表中，先取通讯录所有人员
        members = self.driver.find_elements_by_xpath(
            '//*[@resource-id="com.tencent.wework:id/dec"]//*[@class="android.widget.TextView"]')
        # 现有人员列表
        mem_list = [member.get_attribute("text") for member in members]
        # print(mem_list)
        # 验证已删人员不在列表中
        assert username not in mem_list