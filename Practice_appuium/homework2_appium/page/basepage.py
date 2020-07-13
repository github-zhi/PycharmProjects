from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver: WebDriver = None):
        self._driver = driver

    def find(self, locator):
        return self._driver.find_element(*locator)


    def find_and_click(self, locator):
        return self._driver.find_element(*locator).click()


    def find_and_sendkeys(self, locator, value):
        return self._driver.find_element(*locator).send_keys(value)



    def find_by_scroll(self, text):
        return self._driver.find_element\
            (MobileBy.ANDROID_UIAUTOMATOR,
             'new UiScrollable(new UiSelector().scrollable(true).' 
             f'instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));').click()

    def find_and_wait(self, text):
        return WebDriverWait(self._driver, 5, 0.5).until_not\
            (lambda x: x.find_element_by_xpath(f"//*[@text='{text}']"))

    def back(self, num=1):
        for i in range(num):
            self._driver.back()


