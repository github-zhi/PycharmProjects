import unittest

class Demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setup_class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("TearDownClass")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("test_case01")
        self.assertEqual(1, 1, "判断相等")
        # 第一个判断正确，后面的判断才有意义
        self.assertIn('h', 'hello')

    @unittest.skipIf(1+1==2, "跳过")
    def test_case02(self):
        print("test_case02")
        self.assertEqual(2, 3, "判断相等")
        self.assertIn('h', 'hello')

    def test_case03(self):
        print("test_case03")
        self.assertEqual(3, 3, "判断相等")
        self.assertNotIn('h', 'year')

class Demo1(unittest.TestCase):

    def test_case04(self):
        print("test_case04")
        self.assertEqual(3, 3, "判断相等")

    def test_case05(self):
        print("test_case05")
        self.assertEqual(3, 3, "判断相等")

class Demo2(unittest.TestCase):

    def test_case04(self):
        print("test_case06")
        self.assertEqual(3, 3, "判断相等")

    def test_case05(self):
        print("test_case07")
        self.assertEqual(3, 3, "判断相等")


if __name__ == '__main__':

    # # 执行方法一：使用main可以对本模块里所有以test开始的方法进行执行
    # unittest.main()

    # # 执行方法二：加入容器中执行。只针对部分用例执行
    # # 设置容器
    # suite = unittest.TestSuite()
    # # 添加要执行的（类（方法））
    # suite.addTest(Demo("test_case01"))
    # suite.addTest(Demo1("test_case05"))
    # # 执行
    # unittest.TextTestRunner().run(suite)

    # # 执行方法三：同时测多个类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(Demo2)
    # suite = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner(verbosity=2).run(suite)

    # 执行方法四：匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
    # 被测脚本路径
    test_dir = './test_case'
    # pattern脚本名称匹配规则
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')