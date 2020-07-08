import pytest
import yaml

class TestData:
    def test_data(self):
        a, b = 1, 3
        print(a+b)

    # 参数化：string
    @pytest.mark.parametrize("a, b", [(1, 2), (10, 20), (100, 200)])
    def test_param(self, a, b):
        print(a + b)

    # 参数化：元组tuple
    @pytest.mark.parametrize(("a", "b"), [(1, 2), (3, 4), (5, 6)])
    def test_param(self, a, b):
        print(a + b)

    # 参数化：list。tuple与list的区别：在其后加.联想出来的是不一样的。
    @pytest.mark.parametrize(["a", "b"], [(2, 2), (3,3), (5, 6)])
    def test_param(self, a, b):
        print(a + b)

    # 参数化：yaml加载，配合tuple、list参数，使用string会报错
    @pytest.mark.parametrize(["a", "b"], yaml.safe_load(open("./data1.yaml")))
    def test_param(self, a, b):
        print(a + b)
