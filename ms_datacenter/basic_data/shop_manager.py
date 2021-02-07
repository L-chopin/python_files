import random
from ms_datacenter.common.login_api import login


class Shop:

    @classmethod
    def get_shop_id(cls):
        session = login.get_session()
        response = session.get("http://14.23.109.84:9092/shopMange/selectScreen")
        shop_id_list = []

        for i in response.json()["data"]["list"]:
            shop_id_list.append(i["shopId"])

        shop_id = random.choice(shop_id_list)

        return shop_id

    @classmethod
    def get_shop_name(cls):
        session = login.get_session()
        response = session.get("http://14.23.109.84:9092/shopMange/selectScreen")
        shop_name_list = []

        for i in response.json()["data"]["list"]:
            shop_name_list.append(i["shopName"])

        shop_name_list.remove("SF苏宁")

        shop_name = random.choice(shop_name_list)
        return shop_name

    @classmethod
    def get_shop_list(cls):
        session = login.get_session()
        response = session.get("http://14.23.109.84:9092/shopMange/selectScreen")
        shop_list = response.json()["data"]["list"]
        return shop_list
