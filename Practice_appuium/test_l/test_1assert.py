from appium import webdriver # 引入依赖包appium
from time import sleep # 引入等待时间
# capabilities设置
desired_caps = {
    'platformName': 'Android',
    'platformVersion': "6.0",
    'deviceName': "127.0.0.1:7555",
    'appPackage': "com.android.settings",
    'appActivity': "com.android.settings.Settings"
}

# 初始化driver
dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
dr.quit()