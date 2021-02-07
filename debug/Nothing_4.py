from debug.Nothing_5 import RandomProvinceAndCity0
import random

all_provinces = RandomProvinceAndCity0.get_province_and_city()[0]
all_cities = RandomProvinceAndCity0.get_province_and_city()[1]

i = 1

while i <= 1:
    province_list = all_provinces
    city_list = all_cities
    province = []
    city = []

    # 随机取省的个数，1-5个
    m = random.randint(1, 5)
    for i in range(m):
        # 随机取【id，省份】
        random_province = random.choice(province_list)
        # 通过索引获取省份名，把取过的省份从列表中移除，避免取重复的省份
        # province = random_province[1]

        province.append(random_province[1])

        province_list.remove(random_province)

        print(province)













        # # 取城市
        # n = random.randint(1, 5)
        # for j in range(n):
        #     if random_province[0] != 81 or random_province[0] != 82:
        #         random_city = random.choice(city_list)
        #         city.append(random_city[1])
        #         city_list.remove(random_city)



        # print(city)


        # # 通过id，判断省份是否为“香港”或者“澳门”，是的话直接返回
        # if random_province[0] == 81 or random_province[0] == 82:
        #     province_and_city[province] = ""
        # else:
        #     # 非“香港”或者“澳门”的省份，根据pid查询获取的省份对应的所有城市
        #     sql = "SELECT `name` FROM `province_city_district` WHERE pid = %d" % random_province[0]
        #     cursor.execute(sql)
        #     rows2 = cursor.fetchall()
        #
        #     # 定义一个空的“城市”列表，遍历所有数据，转换为列表类型，并将转换类型后的数据加入到“城市”列表中
        #     cities = []
        #     for j in rows2:
        #         a = list(j)
        #         cities.append(a[0])
        #
        #     # 定义一个空的“城市”列表
        #     city = []
        #     n = random.randint(1, 5)  # 随机取城市的个数，1-5个
        #     for i in range(n):
        #         # 随机取“城市”，将获取到的城市加入到city列表中，并从cities删除该城市，避免取重复城市
        #         random_city = random.choice(cities)
        #         city.append(random_city)
        #         cities.remove(random_city)
        #     # 将获取的省份和对应城市存入字典中
        #     province_and_city[province] = city