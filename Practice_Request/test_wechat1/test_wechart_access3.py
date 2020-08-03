import pytest
import requests
import yaml


class TestWeworkAccess:

    with open('./wechat.yml', 'r+', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        print(datas)

    # 调用session方法，跨请求保持数据
    s = requests.Session()

    def setup(self):
        params = {
            "corpid": "wwa2312efc6d7ac352",
            "corpsecret": "gPio7a6RyBtJMDcXkSckWkpeFyQmC3eDdHHtM6J3jrc"
        }
        r = self.s.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        # 将数据参数更新保存token,跨请求的时候直接带入
        self.s.params.update({"access_token": r.json()["access_token"]})

    @pytest.mark.parametrize(('userid', 'name', 'mobile', 'department'), datas['add'])
    # 创建成员
    def test_add(self, userid, name, mobile, department):
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        # 请求参数使用
        res = self.s.post(url='https://qyapi.weixin.qq.com/cgi-bin/user/create', json=data)
        print(res.json())


    @pytest.mark.parametrize(('userid'), datas['delete'])
    # 删除成员
    def test_delete(self, userid):
        params = {
            "userid": userid
        }
        res = self.s.get(url="https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=params)
        print(res.json())
