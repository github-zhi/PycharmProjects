import pytest
import yaml


@pytest.fixture(scope='session')
def login():
    print("---登录")
    yield ['aa_bb', '11-22']
    print("退出操作---")

@pytest.fixture(scope='session')
def ca():
    print("---开始计算")
    yield ['cc', '33']
    print("计算结束---")


def pytest_addoption(parser):
    mygroup = parser.getgroup("zhizhi")
    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='what are you 弄啥呀！'
                      )
# @pytest.fixture(scope='session')
# def cmdoption(request):
#     return request.config.getoption("--env", default='test')

@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        print("获取Test数据")
        with open("./env_test.yaml") as f:
            datas = yaml.safe_load(f)
    elif myenv == 'dev':
        print("取Dev-data")
        with open("./env_dev.yaml") as f:
            datas = yaml.safe_load(f)
    return datas