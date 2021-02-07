# 基于中台测试库"ms_datacenter"，`province_city_district`表
# 获取随机个数的省份和城市

import pymysql


class RandomProvinceAndCity:

    @classmethod
    def get_province_and_city(cls):
        # 定义一个空的“省份和城市”列表
        province_and_city_list = []
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

        # 编写sql，查询所有的省份和对应的id
        sql1 = "SELECT id,`name` FROM `province_city_district` WHERE pid = 0"
        # 执行sql
        cursor.execute(sql1)

        # 获取所有【id，省份】数据
        rows1 = cursor.fetchall()
        # 定义一个空的“省份”列表，遍历所有数据，转换成列表类型，并将数据加入“省份”列表中
        provinces = []
        for i in rows1:
            a = list(i)
            provinces.append(a)
        province_and_city_list.append(provinces)

        # 编写sql，查询所有的城市和对应的id
        sql2 = "SELECT id,`name` FROM `province_city_district` WHERE LENGTH(id) = 6"
        # 执行sql
        cursor.execute(sql2)

        # 获取所有【id，省份】数据
        rows2 = cursor.fetchall()
        # 定义一个空的“省份”列表，遍历所有数据，转换成列表类型，并将数据加入“省份”列表中
        cities = []
        for i in rows2:
            b = list(i)
            cities.append(b)
        province_and_city_list.append(cities)

        return province_and_city_list
