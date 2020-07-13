from appium import webdriver

from app_LS2.test_wechat3.page.basepage import BasePage
from app_LS2.test_wechat3.page.main_page import MainPape


class App(BasePage):
    # def __init__(self, driver:WebDriver=None):
    #     self._driver = driver

    def start(self):
        if self._driver == None:
            caps = {"deviceName": "127.0.0.1:7555",
                    "platformName": "Android",
                    "appPackage": "com.tencent.wework",
                    "appActivity": ".launch.LaunchSplashActivity",
                    "noReset": "true"}
            # 创建驱动
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # launch_app()启动的是caps里定义的Activity
            self._driver.launch_app()
        # 隐式等待
        self._driver.implicitly_wait(5)
        return self

    def restart(self):
        pass

    def close(self):
        self._driver.quit()

    def goto_mainpage(self):
        self._driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        return MainPape(self._driver)