# 营销分析-广告投放商品日报表
import random
import datetime
import pandas as pd
from ms_datacenter.basic_data.shop_manager import Shop
from ms_datacenter.basic_data.ad_type import adType
from ms_datacenter.basic_data.product_data import product


data_list = []

# 设置初始日期
date_time = datetime.date(2021, 1, 1)

# 设置日期增量
date_delta = datetime.timedelta(days=1)

i = 1

while i <= 5:

    base_list = []

    # 日期
    if i != 1:
        date_time = date_time + date_delta

    # 店铺ID
    shop_id_list = Shop.get_shop_id()
    shop_id = random.choice(shop_id_list)
    # shop_id = "1CK00001"

    # 广告类型
    ad_type_list = adType.get_adType()
    ad_type = random.choice(ad_type_list)
    # ad_type = "小兵的广告类型"

    # 商品ID
    product_id = product.get_product_id(shopId=shop_id)

    # 成交金额
    transaction_amount = random.uniform(1, 7000)

    # 总费用
    cost_all = random.uniform(1, 10000)

    # 支付件数
    payments_num = random.randint(0, 50)

    print("日期：%s  店铺ID:%s  广告类型：%s  商品ID：%s  成交金额：%.2f  总费用：%.2f  支付件数：%d" %
          (date_time, shop_id, ad_type, product_id, transaction_amount, cost_all, payments_num))

    base_list.append(date_time)
    base_list.append(shop_id)
    base_list.append(ad_type)
    base_list.append(product_id)
    base_list.append(round(transaction_amount, 2))
    base_list.append(round(cost_all, 2))
    base_list.append(payments_num)

    data_list.append(base_list)

    i += 1

df = pd.DataFrame(data_list, columns=["日期", "店铺ID", "广告类型", "商品ID", "成交金额", "总费用", "支付件数"])
df.to_excel('D://python导出表格/线上店铺数据/营销分析/广告投放商品日报表==测试用.xlsx',index=False)
