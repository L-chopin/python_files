# 获取素材名称（通过接口）

import random
from ms_datacenter.common.login_api import Login


class GetMaterial:

    @classmethod
    def material_name(cls):
        # 输入用户名和密码，调用Login的get_token方法获取token
        session = Login.get_session()

        response = session.get("http://192.168.10.16:9092/adPlan/findAllMedia")

        material_name_list = []
        i = 0
        while i < len(response.json()["data"]):
            material_name_list.append(response.json()["data"][i]["name"])
            i += 1

        material_name = random.choice(material_name_list)

        return material_name

    @classmethod
    def get_material_list(cls):
        # 输入用户名和密码，调用Login的get_token方法获取token
        session = Login.get_session()

        response = session.get("http://192.168.10.16:9092/adPlan/findAllMedia")
        material_list = response.json()["data"]
        return material_list
