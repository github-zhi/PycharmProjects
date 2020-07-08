import pytest
import yaml

from pytest_homework1.t_cal import Calculator

class TestCal:

    def setup_class(self):
        self.cal = Calculator()
        print("setup class")

    def teardown_class(self):
        print("teardown class")

    # 加法add,方法上参数化
    @pytest.mark.parametrize("a, b, r",
                             [(1, 2, 3), (-1, -2, -3),
                              (9999, 8888, 18887),
                              (1.1, 2.2, 3.3)])
    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='add')
    def test_add(self, ca, a, b, r):
        assert r == self.cal.add(a, b)

    # 减法subtraction
    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends='add')
    def test_sub(self, ca):
        assert 3 == self.cal.sub(5, 2)

    # 乘法multiplication
    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='mul')
    def test_mul(self, ca):
        assert 10 == self.cal.mul(5, 2)

    # 除法subtraction
    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends='mul')
    def test_div0(self, ca):
        assert 2 == self.cal.div(4, 2)

# 类上参数化
@pytest.mark.parametrize("a, b, r",
                         [(1, 2, 3), (100, 200, 300), (1000, 2000, 3000),
                          (-1, -2, -3), (-100, -200, -300), (-10, 20, 10),
                          (0.1, 0.2, 0.3), (1.1, 0.2, 1.3), (10.1, 0.2, 10.3)])
class TestCal1:

    def setup_class(self):
        self.cal = Calculator()
        print("setup class")

    def teardown_class(self):
        print("teardown class")

    # 加法add,方法上参数化

    def test_add(self, ca, a, b, r):
        assert r == self.cal.add(a, b)

    def test_add1(self, ca, a, b, r):
        assert r == self.cal.add(a, b)


# 类上参数化,使用yaml
class TestCal2:

    def setup_class(self):
        self.cal = Calculator()
        print("setup class")

    def teardown_class(self):
        print("teardown class")

    # 参数化：yaml加载，配合tuple、list参数，使用string会报错
    @pytest.mark.parametrize(["a", "b", "r"], yaml.safe_load(open("./data.yaml")))
    # 减法subtraction
    def test_sub(self, ca, a, b, r):
        assert r == self.cal.sub(a, b)

