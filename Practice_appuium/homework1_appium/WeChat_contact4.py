from time import sleep

import pytest
import yaml
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestWechat:

    def setup_class(self):
        caps = {"deviceName": "127.0.0.1:7555",
                "platformName": "Android",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": "true"}
        # 创建驱动
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        # 关闭这个session
        self.driver.quit()

    with open('./data.yaml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        # print(datas)
        addlist = datas['add']
        dellist = datas['del']

    @pytest.mark.parametrize('username, gender, phonenum', addlist)
    def test_addcontact(self, username, gender, phonenum):
        # 1、要添加的人员信息
        # username = "李小龙"
        # gender = '男'
        # phonenum = '19907040003'

        # 2、点击通讯录
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        sleep(3)

        # 3、找到添加成员，点击添加成员
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
        sleep(1)
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
        self.driver.back()

    @pytest.mark.parametrize('username, gender, phonenum', dellist)
    def test_delcontact(self, username, gender, phonenum):
        # 1、要删除人员的姓名
        # username = "张菲"
        # 2、点击通讯录
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        # 3、找到要删除的人员(优化：如果能查到，则执行；查不到，跳过)
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("{username}").instance(0));').click()
        # 4、点击右上角，进入个人信息
        self.driver.find_element_by_xpath(
            '//*[@text="个人信息"]/../../../../..//*[@class="android.widget.RelativeLayout"]').click()
        # 5、编辑成员（优化：所有元素最好显式等待）
        self.driver.find_element_by_xpath('//*[@text="编辑成员"]').click()
        # 6、删除成员
        # self.driver.find_element_by_android_uiautomator(
        #     f'new UiScrollable(new UiSelector().scrollable(true)\
        #     .instance(0)).scrollIntoView(new UiSelector().\
        #     text("删除成员").instance(0));').click()
        self.driver.find_element_by_xpath('//*[@text="删除成员"]').click()
        # 7、确定删除
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        # 8、验证已删除人员不在列表中，先取通讯录所有人员
        WebDriverWait(self.driver, 10, 0.5).until_not(lambda x: x.find_element_by_xpath(f"//*[@text='{username}']"))