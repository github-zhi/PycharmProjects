import pytest

@pytest.fixture(scope='session')
def login():
    print("使用congtest-session的方式")
    return ['congtest.py', 'scope=session']