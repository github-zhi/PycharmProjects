from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""


    # 初始化，需要传入driver,加上WebDriver标记符，可以在使用driver.时联想出来，没有则不会联想出来，初始值为None
    def __init__(self, driver: WebDriver = None):
        # 默认无值
        self._driver = ""
        # 对driver进行判断,便于调用，只有第一次调用时初始化，后续有driver了，就没必须再初始化。
        if driver is None:
            # 初始化driver
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        # 判断base_url并访问
        if self._base_url != "":
            self._driver.get(self._base_url)

        self._driver.maximize_window()
        self._driver.implicitly_wait(5)


    # 封装一个查找元素的方法
    def find(self, by, locator):
        return self._driver.find_element(by, locator)
