import time
from test_l.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        # 所有窗口
        windows = self.driver.window_handles
        # 切换到目标窗口
        self.driver.switch_to_window(windows[-1])
        # 再定位元素进行操作，如果不是目标窗口，则找不到操作元素
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("zhi")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("19906190000")

        self.driver.switch_to_window(windows[0])
        time.sleep(2)
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("aaaaaa")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("111111")
        time.sleep(2)

class TestFrame(Base):
    def test_frame(self):
        '''
        frame存在两种：一种是嵌套的，一种是未嵌套的
        切换frame
            driver.switch_to.frame() # 根据元素id或index切换frame
            driver.switch_to.default_content() # 切换到默认frame
            driver.switch_to.parent_frame() # 切换到父级frame
        未嵌套的iframe
            driver.switch_to_frame("frame的id")
            driver.switch_to_frame("frame-index")索引从0开始
        :return:
        '''
        # self.driver.get("https://www.w3school.com.cn/tiy/t.sap?f=html_frame_cols")
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

        self.driver.switch_to.frame("iframeResult")
        # self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("droppable").text)

        self.driver.switch_to.parent_frame()
        # self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)