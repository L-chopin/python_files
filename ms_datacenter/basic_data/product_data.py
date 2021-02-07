import random,pymysql
from ms_datacenter.common.login_api import Login


class Product:

    @classmethod
    def get_product_id(cls,shopId="",shopName=""):

        # 创建连接
        connect = pymysql.Connect(
            host="192.168.10.16",
            port=3306,
            database="ms_datacenter",
            user="root",
            password="Ms77897854",
            charset="utf8"
        )

        # 创建游标
        cursor = connect.cursor()

        # 查询CK所有的店铺
        sql_ck = "SELECT * FROM `shop_manage` WHERE id LIKE '1CK%'"
        cursor.execute(sql_ck)
        ck_rows = cursor.fetchall()
        # 将查询结果筛选，分别赋值给 ID列表 和 店铺名列表
        ckId_list = []
        ckName_list = []
        for i in ck_rows:
            ckId_list.append(i[0])
            ckName_list.append(i[2])


        # 查询SF所有的店铺
        sql_sf = "SELECT * FROM `shop_manage` WHERE id LIKE '1SF%'"
        cursor.execute(sql_sf)
        sf_rows = cursor.fetchall()
        # 将查询结果筛选，分别赋值给 ID列表 和 店铺名列表
        sfId_list = []
        sfName_list = []
        for i in sf_rows:
            sfId_list.append(i[0])
            sfName_list.append(i[2])


        # 查询LAB所有的店铺
        sql_lab = "SELECT * FROM `shop_manage` WHERE id LIKE '1LAB%'"
        cursor.execute(sql_lab)
        lab_rows = cursor.fetchall()
        # 将查询结果筛选，分别赋值给 ID列表 和 店铺名列表
        labId_list = []
        labName_list = []
        for i in lab_rows:
            labId_list.append(i[0])
            labName_list.append(i[2])


        # 根据调用时的参数（不同品牌的商店），返回不同的商品id（对应品牌的商品）
        if shopId in ckId_list or shopName in ckName_list:
            sql = "SELECT DISTINCT product_no FROM `product_manage_data` WHERE product_no LIKE '1C%'"
        elif shopId in sfId_list or shopName in sfName_list:
            sql = "SELECT DISTINCT product_no FROM `product_manage_data` WHERE product_no LIKE '1S%'"
        elif shopId in labId_list or shopName in labName_list:
            sql = "SELECT DISTINCT product_no FROM `product_manage_data` WHERE product_no LIKE '1L%'"
        else:
            sql = "SELECT DISTINCT product_no FROM `product_manage_data`"

        cursor.execute(sql)
        rows = cursor.fetchall()
        product_id_list = []
        for i in rows:
            a = i[0]
            product_id_list.append(a)

        product_id = random.choice(product_id_list)

        return product_id

    # 获取商品字典，分品牌（不含组合装）
    @classmethod
    def get_product_dict(cls):
        product_dict = {}
        colorkey_product_list = []
        superface_product_list = []
        lab101_product_list = []
        session = Login.get_session()
        response = session.get("http://192.168.10.16:9092/pmd/selectScreen")
        product_list = response.json()["data"]["list"]
        for i in product_list:
            if i["productNo"][:2] == "1C":
                colorkey_product_list.append(i)
            elif i["productNo"][:2] == "1S":
                superface_product_list.append(i)
            elif i["productNo"][:2] == "1L":
                lab101_product_list.append(i)
        product_dict["colorkey"] = colorkey_product_list
        product_dict["superface"] = superface_product_list
        product_dict["lab101"] = lab101_product_list

        return product_dict
