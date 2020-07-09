# input标签可以直接使用send_keys（文件地址）上传文件
# 用法：
#     el = driver.find_element_by_id("上传按钮")
#     el.send_keys("文件路径+文件名")
from selenium.webdriver import ActionChains

from test_l.base import Base

class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("http://image.baidu.com/")
        # 定位上传按钮
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("uploadImg").send_keys(r"C:\Users\dell\Pictures\bald-eagle-2715461_1280.jpg")

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 根据元素id或index切换frame
        self.driver.switch_to_frame("iframeResult")
        # 元素拖拽
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        # 点击alert确认
        self.driver.switch_to.alert.accept()
        # 点击重新运行
        self.driver.switch_to.default_content() # 切换到父级frame
        self.driver.find_element_by_id("submitBTN").click()

''''
弹框处理机制
页面操作中遇到JS所生成的alert/confirm/prompt弹框，可以使用switch_to.alert()方法定位到。然后使用text/accept/dismiss/send_keys
等方法进行操作。先分辨alert/window/div模态框，以及操作。
操作alert常用方法：
    switch_to.alert():获取当前页面上的警告框。
    text：返回alert/confirm/prompt中的文字信息。
    accept():接受现有警告框。
    dismiss():解散现有警告框。
    send_keys(KeysToSend):发送文本至警告框。
'''


