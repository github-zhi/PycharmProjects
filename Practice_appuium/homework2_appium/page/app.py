from appium import webdriver
from homework2_appium.page.basepage import BasePage
from homework2_appium.page.main_page import MainPage


class App(BasePage):
    
    def start(self):
        if self._driver is None:
            desire_cap = {
                "platformName": "Android",
                "platformVersion": "6.0.1",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": "com.tencent.wework.launch.WwMainActivity",
                "noReset": True,
                "skipDeviceInitialization": True,
                "unicodeKeyBoard": True,
                "resetKeyBoard": True
            }
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        else:
            self._driver.launch_app()
        
        self._driver.implicitly_wait(10)
        return self

    def close(self):
        self._driver.quit()

    def main(self):
        return MainPage(self._driver)