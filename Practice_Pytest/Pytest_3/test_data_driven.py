import pytest
import yaml


class TestDataDriven:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./data2.yaml")))
    def test_data_driven(self, env):
        if "test" in env:
            print("这是测试环境")
            print(env)
        elif "dev" in env:
            print("开发环境。")
            print(env)
        else:
            print("不知道什么环境！")
            print(env)

    def test_yaml(self):
        print(yaml.safe_load(open("./data2.yaml")))