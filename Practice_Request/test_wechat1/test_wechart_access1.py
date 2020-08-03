import requests


class TestWeworkAccess:

    # 接口信息 https://work.weixin.qq.com/api/doc/90000/90135/91039
    # 企业ID:wwa2312efc6d7ac352
    # Secret:gPio7a6RyBtJMDcXkSckWkpeFyQmC3eDdHHtM6J3jrc

    def test_get_token(self):
        # 直接把参数值放到请求中
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwa2312efc6d7ac352"
                           "&corpsecret=gPio7a6RyBtJMDcXkSckWkpeFyQmC3eDdHHtM6J3jrc")
        # print(res.json())
        # 提取token
        # print(res.json()['access_token'])
        return res.json()['access_token']

    # 创建成员
    def test_add(self):

        data = {
            "userid": "basanyi",
            "name": "八三一",
            "mobile": "19908030001",
            "department": [2]
        }
        # 请求参数使用
        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_get_token()}",
                            json=data)
        print(res.json())

    # 读取成员
    def test_get(self):
        params = {
            "access_token": self.test_get_token(),
            "userid": "basanyi"
        }
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get", params=params)
        print(res.json())

    # 更新成员
    def test_update(self):
        data = {
            "userid": "basanyi",
            "name": "八三二",
        }
        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.test_get_token()}",
                            json=data)
        print(res.json())

    # 删除成员
    def test_delete(self):
        params = {
            "access_token": self.test_get_token(),
            "userid": "basanyi"
        }
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=params)
        print(res.json())
