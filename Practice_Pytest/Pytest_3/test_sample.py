import pytest

def inc(x):
    return x + 1

# 这种是以pytest解释器执行
def test_answer():
    assert inc(4) == 5

class TestDemo:
    def test_a(self):
        print("a")

    def test_b(self):
        print("a")

    # 不以test开头，不会执行
    def c(self):
        print("a")

def fun(x):
    return x + 1
class TestDemo1():
    @pytest.mark.parametrize("a, b", [(1, 2), (3, 4), (5, 6)])
    def test_answer1(self, a, b):
        assert fun(a) == b

# 这是python解释器的入口函数
if __name__ == '__main__':
    pytest.main(["test_sample.py"])