# 淘宝客团长商品数据

import random,datetime
import pandas as pd
from ms_datacenter.basic_data.product_data import product
from utils.list_str_concat import list_to_str

data_list = []

# 设置初始日期
date_time = datetime.date(2020, 10, 1)

# 设置日期增量
date_delta = datetime.timedelta(days=1)

i = 1

while i <= 100:

    base_list = []

    # 日期
    if i != 1:
        date_time = date_time + date_delta

    # 店铺ID
    shop_id_list = ["1CK00001","1SF00001","1LAB00001"]
    # shop_id = "1CK00001"
    shop_id = random.choice(shop_id_list)

    # 商品ID
    product_id = list_to_str.get_str(product.get_product_id(shopId=shop_id))

    # 点击量
    clicks = random.randint(0,2000)

    # 支付笔数
    payments_number = random.randint(0,clicks)

    # 商品单价
    price = random.uniform(9,69)

    # 成交金额
    gvm = payments_number*price

    # 结算笔数
    receipt_number = random.randint(0,payments_number)

    # 结算金额
    receipt_amount = receipt_number*price

    # 佣金费用
    commission = receipt_amount*random.uniform(0,1)

    # 服务费用
    service_fee = random.uniform(0,commission)

    # 优惠券使用张数
    coupons_used = random.randint(0,100)

    print("日期：%s  店铺ID：%s  商品ID：%s  点击量：%d  支付笔数：%d  成交金额：%.2f  结算笔数：%d  结算金额：%.2f  佣金费用：%.2f  服务费用：%.2f  优惠券使用张数：%d" %
          (date_time,shop_id,product_id,clicks,payments_number,gvm,receipt_number,receipt_amount,commission,service_fee,coupons_used))

    base_list.append(date_time)
    base_list.append(shop_id)
    base_list.append(product_id)
    base_list.append(clicks)
    base_list.append(payments_number)
    base_list.append(round(gvm,2))
    base_list.append(receipt_number)
    base_list.append(round(receipt_amount,2))
    base_list.append(round(commission,2))
    base_list.append(round(service_fee,2))
    base_list.append(coupons_used)

    data_list.append(base_list)

    i += 1

df = pd.DataFrame(data_list,columns=["日期","店铺ID","商品ID","点击量","支付笔数","成交金额","结算笔数","结算金额","佣金费用","服务费用","优惠券使用张数"])

df.to_excel('D://python导出表格/线上店铺数据/联盟数据/淘宝客团长商品数据==测试用.xlsx',index=False)