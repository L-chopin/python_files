# 获取广告类型

from ms_datacenter.common.login_api import login


class AdType:

    @classmethod
    def get_ad_type(cls):
        session = login.get_session()

        json = {
            "bsDictType": "adType"
        }

        response = session.post("http://192.168.10.16:9092/bsDict/selectByType", json=json)
        ad_type_list = []

        for i in response.json()["data"]["list"]:
            ad_type_list.append(i["bsDictValue"])

        return ad_type_list
