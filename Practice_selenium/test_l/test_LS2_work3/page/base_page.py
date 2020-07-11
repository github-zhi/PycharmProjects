from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    # 把变的url放到index中，用参数传过来
    _base_url = ""
    # 每次return时，还需要调用driver，此时加上参数并判断
    # 添加WebDriver标记符，可以在使用driver.时联想出来，没有则不会联想出来，导入from selenium.webdriver.remote.webdriver import WebDriver

    def __init__(self, driver_base: WebDriver = None):

        if driver_base == None:
            # 实例化options
            option = Options() # 导入包from selenium.webdriver.chrome.options import Options
            # 启动命令windows：chrome --remote-debugging-port=9222
            # 启动命令mac：Google\ Chrome --remote-debugging-port=9222
            # 需要和启动命令的端口号一致
            # 指定了一个调试地址
            option.debugger_address = "localhost:9222"
            # 实例变量，加self
            self.driver = webdriver.Chrome(options=option) # 导入包from selenium import webdriver

        else:
            self.driver = driver_base

        if self._base_url != "":
            self.driver.get(self._base_url)

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # 在basepage中封装一个find方法，供其它调用，driver.find_element处直接使用find即可。
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # driver.find_elements处直接使用finds即可
    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    # 退出
    def quit(self):
        self.driver.quit()

    # 显示等待封装
    def wait_until_clickable(self, by, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((by, locator)))

    def wait_until_located(self, by, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((by, locator)))
