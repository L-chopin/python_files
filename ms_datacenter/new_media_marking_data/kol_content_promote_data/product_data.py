# 达人内容推广商品数据

import random
import datetime
import pandas as pd
from ms_datacenter.basic_data.product_data import product

data_list = []


# 设置初始日期
date = datetime.date(2021, 1, 31)

# 设置日期增量
date_increment = datetime.timedelta(days=1)

i = 1

while i <= 10:

    base_list = []

    # 日期
    if i != 1:
        date = date + date_increment

    # 渠道
    channel_list = ["抖音", "小红书"]
    channel = random.choice(channel_list)

    if channel == "抖音":
        # 平台
        platform = "天猫"

        # 店铺
        shop_list = ["colorkey天猫", "surperface天猫", "瑞沛天猫"]
        shop = random.choice(shop_list)
    else:
        # 平台
        platform = "小红书"

        # 店铺
        shop_list = ["colorkey小红书2", "colorkey抖音旗舰店", "superface小红书", "瑞沛小红书"]
        shop = random.choice(shop_list)

    # 商品ID
    product_id = product.get_product_id(shopName=shop)

    # 成交金额（达人淘宝客）
    gvm_taoke = random.uniform(0, 1500)

    print("日期：%s  渠道：%s  平台：%s  店铺：%s  商品ID：%s  成交金额（达人淘宝客）:%.2f" %
          (date, channel, platform, shop, product_id, gvm_taoke))

    base_list.append(date)
    base_list.append(channel)
    base_list.append(platform)
    base_list.append(shop)
    base_list.append(product_id)
    base_list.append(round(gvm_taoke, 2))

    data_list.append(base_list)

    i += 1

df = pd.DataFrame(data_list, columns=["日期", "渠道", "平台", "店铺", "商品ID", "成交金额（达人淘宝客）"])
df.to_excel("D://python导出表格/新媒体营销数据/达人内容推广数据/达人推广商品数据==测试用.xlsx", index=False)
