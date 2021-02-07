# 商品优惠券数据汇总

import random
import datetime
import pandas as pd
from faker import Faker
from ms_datacenter.basic_data.shop_manager import Shop
from ms_datacenter.common.login_api import login

fake = Faker("zh_CN")

session = login.get_session()

data_list = []

i = 1

while i <= 3:
    base_list = []

    # 日期
    date = datetime.date(2021, 1, 1)

    # 店铺
    shopName = Shop.get_shop_name()

    # 平台
    params = {
        "shopName": shopName
    }
    response1 = session.get("http://14.23.109.84:9092/shopMange/selectScreen", params=params)
    platform = response1.json()["data"]["list"][0]["platform"]

    # 优惠券名称
    coupon_name = ""

    # 成交金额
    gvm = random.uniform(0, 2000)

    # 领取数量
    received_number = random.randint(0, 100)

    # 使用张数
    coupons_used = random.randint(0, received_number)

    # 支付买家数
    payments_buyer = random.randint(0, 50)

    # 支付件数
    payments_number = random.randint(payments_buyer, 150)

    # 备注
    remark_list = ["", fake.paragraph()]
    remark = random.choice(remark_list)

    print("日期：%s  平台：%s  店铺：%s  优惠券名称：%s  成交金额：%.2f  领取数量：%s  使用张数：%s  支付件数：%s  支付买家数：%s  备注：%s" %
          (date, platform, shopName, coupon_name, gvm, received_number, coupons_used, payments_number, payments_buyer,
           remark))

    base_list.append(date)
    base_list.append(platform)
    base_list.append(shopName)
    base_list.append(coupon_name)
    base_list.append(round(gvm, 2))
    base_list.append(received_number)
    base_list.append(coupons_used)
    base_list.append(payments_number)
    base_list.append(payments_buyer)
    base_list.append(remark)

    data_list.append(base_list)

    i += 1

df = pd.DataFrame(data_list, columns=["日期", "平台", "店铺", "优惠券名称", "成交金额", "领取数量", "使用张数", "支付件数", "支付买家数", "备注"])
df.to_excel("D://python导出表格/线上店铺数据/营销分析/商品优惠券明细==测试用.xlsx", index=False)
