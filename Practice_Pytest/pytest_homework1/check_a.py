import pytest

def test_a():
    print("check文件名")

class CheckDemo:
    def check_a(self):
        print("check类")

def test_b(cmdoption):
    print(f"{cmdoption}")