import random,pymysql

class get_product:

    @classmethod
    def product_id(cls,shopId="",shopName=""):

        # 创建连接
        connect = pymysql.Connect(
            host="14.23.109.84",
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
            sql = "SELECT DISTINCT product_no FROM `product_manage_data` WHERE shop_name = 'COLORKEY珂拉琪'"
        elif shopId in sfId_list or shopName in sfName_list:
            sql = "SELECT DISTINCT product_no FROM `product_manage_data` WHERE shop_name = 'SUPERFACE秀芭菲'"
        elif shopId in labId_list or shopName in labName_list:
            sql = "SELECT DISTINCT product_no FROM `product_manage_data` WHERE shop_name = 'LAB101瑞沛'"
        else:
            sql = "SELECT DISTINCT product_no FROM `product_manage_data`"

        cursor.execute(sql)
        rows = cursor.fetchall()
        product_id_list = []
        for i in rows:
            a = list(i)
            product_id_list.append(a)

        product_id = random.choice(product_id_list)

        return product_id
