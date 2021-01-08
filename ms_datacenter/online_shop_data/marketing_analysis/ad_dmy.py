import random,datetime
import pandas as pd

data_list = []

# 设置初始日期
date_time = datetime.date(2020, 1, 1)

# 设置日期增量
date_delta = datetime.timedelta(days=1)


i = 1

while i <= 3:

    base_list = []

    # 日期
    if i != 1:
        date_time = date_time + date_delta

    # 店铺ID
    shop_id = "1CK00001"

    # 广告类型
    ad_type_list = ["小兵的广告类型","大头兵的广告类型","超级兵的广告类型"]
    ad_type = "超级兵的广告类型"#random.choice(ad_type_list)

    # 成交金额
    gvm = random.uniform(1,1000)

    # 总费用
    total_cost = random.uniform(gvm,1500)

    print("日期:%s  店铺ID:%s  广告类型:%s  成交金额:%.2f  总费用:%.2f" % (date_time,shop_id,ad_type,gvm,total_cost))

    base_list.append(date_time)
    base_list.append(shop_id)
    base_list.append(ad_type)
    base_list.append(round(gvm,2))
    base_list.append(round(total_cost,2))

    data_list.append(base_list)

    i += 1

df = pd.DataFrame(data_list,columns=["日期","店铺ID","广告类型","成交金额","总费用"])

df.to_excel('D:\python导出表格\线上店铺数据\营销分析\广告投放日月年报表==测试用.xlsx',index=False)