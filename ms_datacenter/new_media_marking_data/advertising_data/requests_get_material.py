
import requests,random

from ms_datacenter.login_api import login

class get_material_name:

    @classmethod
    def material_name(cls):
        # 输入用户名和密码，调用Login的get_token方法获取token
        token = login.get_token(username="admin",password="123456")

        # 构造请求头
        headers = {
            "token":token
        }

        # 访问素材查询接口，并接收响应
        response = requests.get("http://47.113.97.130:8081/adPlan/findAllMedia",headers = headers)

        material_name_list = []
        i = 0
        while i < len(response.json()["data"]):
            material_name_list.append(response.json()["data"][i]["name"])
            i += 1

        material_name = random.choice(material_name_list)

        return material_name

