import allure
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 加入allure
@allure.testcase("http://www.github.com")
@allure.feature("百度")
@pytest.mark.parametrize("test_data", ['allure', 'pytest', 'time'])
def test_step_demo2(test_data):
    with allure.step("打开百度"):
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com/')
        driver.maximize_window()
        driver.implicitly_wait(5)

    with allure.step("输入关键词搜索"):
        driver.find_element(By.ID, 'kw').send_keys(test_data)
        time.sleep(2)
        driver.find_element(By.ID, 'su').click()
        time.sleep(3)

    with allure.step("搜索结果截屏"):
        driver.save_screenshot("./report/b.png")
    with allure.step("截屏图片加到报告中"):
        allure.attach.file("./report/b.png", attachment_type=allure.attachment_type.PNG)

    with allure.step("退出"):
        driver.quit()

@pytest.mark.skip()
# 参数化
@pytest.mark.parametrize("test_data", ['a', 'b', 'c'])
def test_step_demo1(test_data):
    driver = webdriver.Chrome()

    driver.get('https://www.baidu.com/')

    driver.find_element(By.ID, 'kw').send_keys(test_data)
    time.sleep(2)
    driver.find_element(By.ID, 'su').click()
    time.sleep(3)

    driver.save_screenshot("./report/b.png")
    driver.quit()

@pytest.mark.skip()
# 最简单的写法
def test_step_demo():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    driver.find_element(By.ID, 'kw').send_keys("tea")
    time.sleep(2)
    driver.find_element(By.ID, 'su').click()
    time.sleep(3)
    driver.save_screenshot("./report/b.png")
    driver.quit()