import requests


class TestWeworkAccess:
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

    # 创建成员
    def test_add(self):
        data = {
            "userid": "basaner",
            "name": "八三二",
            "mobile": "19908030002",
            "department": [2]
        }
        # 请求参数使用
        res = self.s.post(url='https://qyapi.weixin.qq.com/cgi-bin/user/create', json=data)
        print(res.json())

    # 读取成员
    def test_get(self):
        params = {
            "userid": "basaner"
        }
        res = self.s.get(url="https://qyapi.weixin.qq.com/cgi-bin/user/get", params=params)
        print(res.json())

    # 更新成员
    def test_update(self):
        data = {
            "userid": "basaner",
            "name": "八三二A",
        }
        res = self.s.post(url="https://qyapi.weixin.qq.com/cgi-bin/user/update", json=data)
        print(res.json())

    # 删除成员
    def test_delete(self):
        params = {
            "userid": "basaner"
        }
        res = self.s.get(url="https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=params)
        print(res.json())
