import random
from ms_datacenter.common.login_api import Login


class AdAccount:

    @classmethod
    def get_ad_account_id(cls):
        session = Login.get_session()

        response = session.get("http://192.168.10.16:9092/kolpa/selectScreen")
        ad_account_id_list = []

        for i in response.json()["data"]["list"]:
            ad_account_id_list.append(i["accountId"])
            account_id = random.choice(ad_account_id_list)

        return account_id

    @classmethod
    def get_ad_account_name(cls):
        session = Login.get_session()

        response = session.get("http://192.168.10.16:9092/kolpa/selectScreen")
        ad_account_name_list = []

        for i in response.json()["data"]["list"]:
            ad_account_name_list.append(i["accountName"])
            account_name = random.choice(ad_account_name_list)

        return account_name

    @classmethod
    def get_kol_account_list(cls):
        session = Login.get_session()

        response = session.get("http://192.168.10.16:9092/kolpa/selectScreen")
        ad_account_list = response.json()["data"]["list"]
        return ad_account_list
