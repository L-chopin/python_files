# 请求数据中台测试地址登录接口，并返回token
import requests


class Login:

    @classmethod
    def get_session(cls):
        json = {
            "password": "123456",
            "type": "pc",
            "username": "admin"
        }

        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }

        response = requests.post(
            "http://192.168.10.16:9092/sys/login",
            headers=headers,
            json=json
        )

        # 调用.json()方法，将响应信息转变为python字典，不然没法用字典的方式获取响应信息中的token，获取后定义一个新的请求头
        new_header = {"token": response.json()["data"]["accessToken"]}

        # 设置Session对象，把token封装到Session中
        session = requests.Session()
        session.headers.update(new_header)
        return session

