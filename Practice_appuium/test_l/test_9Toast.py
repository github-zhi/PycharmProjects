from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast():
    def setup(self):
        desire = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.view.PopupMenu1",
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        # 打印查看页面中有无Toast
        # print(self.driver.page_source)
        # 打印Toast信息
        # print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, 'Clicked popup')]").text)