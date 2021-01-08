import random,pymysql

class get_material:

    @classmethod
    def material_name(cls):

        # 创建连接
        connect = pymysql.Connect(
            host="14.23.109.82",
            port=3306,
            database="ms_datacenter",
            user="root",
            password="Ms77897854",
            charset="utf8"
        )

        # 创建游标
        cursor = connect.cursor()

        # 编写sql，查询所有的素材名称
        sql = "SELECT DISTINCT product_no FROM product_manage_data"
        # 执行sql
        cursor.execute(sql)
        rows = cursor.fetchall()

        material_name_list = []
        for i in rows:
            a = list(i)
            b = a[0]
            material_name_list.append(a)

        material_name = random.choice(material_name_list)
        return material_name

