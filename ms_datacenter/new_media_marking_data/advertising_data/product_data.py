import random,pymysql

class get_product:

    @classmethod
    def product_id(cls):

        # 创建连接
        connect = pymysql.Connect(
            host="47.113.97.130",
            port=3306,
            database="ms_datacenter",
            user="root",
            password="123456",
            charset="utf8"
        )

        # 创建游标
        cursor = connect.cursor()

        # 编写sql，查询所有的商品ID
        sql = "SELECT DISTINCT product_no FROM product_manage_data"
        # 执行sql
        cursor.execute(sql)
        rows = cursor.fetchall()

        product_id_list = []
        for i in rows:
            a = list(i)
            b = a[0]
            product_id_list.append(a)

        product_id = random.choice(product_id_list)
        return product_id

