import random
import pandas as pd
from utils.random_num_and_letters_code import random_code
from utils.random_name import random_name
from utils.random_number_of_data import random_number_of_data
from utils.random_provinces_and_cities import random_province_and_city
from utils.list_str_concat import list_to_str
from ms_datacenter.new_media_marking_data.advertising_data.product_data import get_product
from ms_datacenter.new_media_marking_data.advertising_data.requests_get_material import get_material_name



data_list = []

z = 1
# 数据量
while z <= 1:
    base_list = []

    # 年龄
    age_list = ["18-23", "24-30", "31-40"]

    # 行为关键词
    behavior_keywords_list = ["知识零售", "消费升级", "下沉市场", "网红带货", "消费分层", "佛系青年", "单身经济", "社交货币", "平台赋能", "线上线下"]

    # 兴趣关键词
    keywos_of_interest_list = ["补水", "抗皱", "祛痘", "美颜", "洁面", "美白", "保湿", "滋润", "防晒", "控油", "遮瑕", "定妆", "精华","面霜","乳液",
                               "洗面奶","面膜","隔离霜","气垫bb","粉底液","色号","唇釉","美妆蛋","眼线笔","定妆喷雾","小金块","小银管"]

    # 手机价格
    phone_price_list = ["0-11000", "500-11000", "1000-11000", "1500-11000", "2000-11000", "2500-11000", "3000-11000"]

    # 行为场景
    behavior_scene_list = ["电商行为场景", "咨询行为场景", "app行为场景"]

    # 人群包
    people_package_dict = {"01": "眼影人群包", "02": "唇釉人群包", "03": "唇膏人群包", "04": "粉底液人群包", "05": "粉底膏人群包", "06": "粉饼人群包",
                           "07": "水乳人群包", "08": "喷雾人群包", "09": "腮红人群包", "10": "眉笔人群包"}



    # 广告账户
    ad_account = "小兵1"

    # 获取名字和性别
    name_and_gender = random_name.get_name_and_gender()

    # 计划名称
    plan_name = '%s的广告投放计划' % name_and_gender[0]

    # 计划ID
    plan_ID = random_code.get_code(6)

    # 淘宝联盟推广账号
    taobao_union_promoted_account = "colorkey旗舰店"

    # 所属推广位
    promotion_position = "小兵的推广位"

    # 商品ID
    product_id = list_to_str.get_str(get_product.product_id())

    # 素材名称
    material_name = get_material_name.material_name()

    # 获取省份和城市
    procince_and_city = random_province_and_city.get_province_and_city()

    # 省份
    province = ""
    i = 0
    while i < len(procince_and_city.keys()) - 1:
        province = province + list(procince_and_city.keys())[i] + "，"
        i += 1
    province = province + list(procince_and_city.keys())[i]

    # 城市
    city = ""
    for values in procince_and_city.values():
        if len(values) != 0:
            y = 0
            while y < len(values) - 1:
                city = city + values[y] + "，"
                y += 1
            city = city + values[y] + "，"
    city = city[:len(city)-1]

    # 性别
    gender = name_and_gender[1]
    # 年龄
    age = list_to_str.get_str(random_number_of_data.get_random_number_of_data(age_list))
    # 行为关键词
    behavior_keywords = list_to_str.get_str(random_number_of_data.get_random_number_of_data(behavior_keywords_list))
    # 兴趣关键词
    keywos_of_interest = list_to_str.get_str(random_number_of_data.get_random_number_of_data(keywos_of_interest_list))
    # 过滤时间
    filtering_time = random.choice(["1个月","3个月","6个月","12个月"])
    # 手机价格
    phone_price = random.choice(phone_price_list)
    # 行为场景
    behavior_scene = list_to_str.get_str(random_number_of_data.get_random_number_of_data(behavior_scene_list))
    # 行为天数
    behavior_days = random.choice(["1","7","15","30","60","90","180"])
    # 获取人群包
    the_people_package = random_number_of_data.get_random_number_of_data(people_package_dict)
    # 人群包ID
    people_package_ID = list_to_str.get_str(list(the_people_package.keys()))
    # 人群包名称
    people_package_name = list_to_str.get_str(list(the_people_package.values()))

    base_list.append(ad_account)
    base_list.append(plan_name)
    base_list.append(plan_ID)
    base_list.append(taobao_union_promoted_account)
    base_list.append(promotion_position)
    base_list.append(product_id)
    base_list.append(material_name)
    base_list.append(province)
    base_list.append(city)
    base_list.append(gender)
    base_list.append(age)
    base_list.append(behavior_keywords)
    base_list.append(keywos_of_interest)
    base_list.append(filtering_time)
    base_list.append(phone_price)
    base_list.append(behavior_scene)
    base_list.append(behavior_days)
    base_list.append(people_package_name)
    base_list.append(people_package_ID)

    data_list.append(base_list)

    print("广告账户：%s  计划名称：%s  计划id：%s  淘宝联盟推广账号：%s  所属推广位：%s  商品id：%s  素材名称：%s  省份：%s  城市：%s  性别：%s  年龄：%s  行为关键词：%s  兴趣关键词：%s  过滤时间：%s  手机价格：%s  行为场景：%s  行为天数：%s  人群包名称：%s  人群包ID：%s" %
      (ad_account,plan_name,plan_ID,taobao_union_promoted_account,promotion_position,product_id,material_name,province,city,gender,age,behavior_keywords,keywos_of_interest,filtering_time,phone_price,behavior_scene,behavior_days,people_package_name,people_package_ID))
    z += 1

df=pd.DataFrame(data_list,columns=['广告账户','计划名称','计划ID','淘宝联盟推广账号','所属推广位','商品ID','素材名称','省份','城市','性别','年龄','行为关键词','兴趣关键词','过滤时间','手机价格','行为场景','行为天数','人群包名称','人群包ID'])   # 将字段和值一一匹配
df.to_excel('D://python导出表格/新媒体营销数据/广告投放数据/广告投放计划管理==测试用.xlsx',index=False)  # 将字段和对应值转化成Excel表格