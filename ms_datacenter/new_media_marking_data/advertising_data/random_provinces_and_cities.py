# 获取随机省份和相应省份的城市

import random
import pymysql


class ProvinceAndCity:

    @classmethod
    def get_province_and_city(cls):
        # 定义一个空的“省份和城市”字典
        province_and_city = {}
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

        # 编写sql，查询所有的省份和对应的id
        sql = "SELECT id,`name` FROM `province_city_district` WHERE pid = 0"
        # 执行sql
        cursor.execute(sql)

        # 获取所有【id，省份】数据
        rows1 = cursor.fetchall()
        # 定义一个空的“省份”列表，遍历所有数据，转换成列表类型，并将数据加入“省份”列表中
        provinces = []
        for i in rows1:
            a = list(i)
            b = a[0]
            provinces.append(a)

        # 随机取省的个数，1-5个
        m = random.randint(1, 5)
        for i in range(m):
            # 随机取【id，省份】
            random_province = random.choice(provinces)
            # 通过索引获取省份名，把取过的省份从列表中移除，避免取重复的省份
            province = random_province[1]
            provinces.remove(random_province)

            # 通过id，判断省份是否为“香港”或者“澳门”，是的话直接返回
            if random_province[0] == 81 or random_province[0] == 82:
                province_and_city[province] = ""
            else:
                # 非“香港”或者“澳门”的省份，根据pid查询获取的省份对应的所有城市
                sql = "SELECT `name` FROM `province_city_district` WHERE pid = %d" % random_province[0]
                cursor.execute(sql)
                rows2 = cursor.fetchall()

                # 定义一个空的“城市”列表，遍历所有数据，转换为列表类型，并将转换类型后的数据加入到“城市”列表中
                cities = []
                for j in rows2:
                    a = list(j)
                    cities.append(a[0])

                # 定义一个空的“城市”列表
                city = []
                # 随机取城市的个数，1-5个
                n = random.randint(1, 5)
                for k in range(n):
                    # 随机取“城市”，将获取到的城市加入到city列表中，并从cities删除该城市，避免取重复城市
                    random_city = random.choice(cities)
                    city.append(random_city)
                    cities.remove(random_city)
                # 将获取的省份和对应城市存入字典中
                province_and_city[province] = city
        # 释放资源
        cursor.close()
        connect.close()
        return province_and_city
