# 达人直播日月年报表

import random
import datetime
import pandas

data_list = []

# 设置初始日期
date_time = datetime.date(2021, 1, 1)

# 设置日期增量
date_delta = datetime.timedelta(days=1)

i = 1

while i <= 4:

    base_list = []

    # 日期
    if i != 1:
        date_time = date_time + date_delta

    # 渠道
    channel_list = ["淘宝", "小红书"]
    channel = random.choice(channel_list)
    channel = "淘宝"

    # 店铺ID

    if channel == "淘宝":
        shop_id_list = ["1CK00001", "1SF00001", "1LAB00001"]
        shop_id = random.choice(shop_id_list)
    elif channel == "小红书":
        shop_id_list = ["1CK00005", "1CK00025", "1LAB00003", "1SF00002"]
        shop_id = random.choice(shop_id_list)
    shop_id = "1CK00001"

    # 今日直播场次
    live_today = random.randint(1, 10)

    # 实际合作费用
    cooperation_costs = random.uniform(10, 200)

    # 预估佣金费用
    commission_costs = random.uniform(10, 200)

    # 成交金额
    gvm = random.uniform(250, 1000)

    # 点击量
    clicks = random.randint(100, 2000)

    # 支付笔数
    payments_number = random.randint(1, 100)

    # 支付件数
    pay_number = payments_number*random.randint(1, 3)

    base_list.append(date_time)
    base_list.append(shop_id)
    base_list.append(channel)
    base_list.append(live_today)
    base_list.append(round(cooperation_costs, 2))
    base_list.append(round(commission_costs, 2))
    base_list.append(round(gvm, 2))
    base_list.append(clicks)
    base_list.append(payments_number)
    base_list.append(pay_number)

    data_list.append(base_list)

    print("日期：%s  店铺ID：%s  渠道：%s  今日直播场次：%d  实际合作费用：%.2f  预估佣金费用：%.2f  成交金额：%.2f  点击量：%d  支付笔数：%d  支付件数；%d" %
          (date_time, shop_id, channel, live_today, cooperation_costs,
           commission_costs, gvm, clicks, payments_number, pay_number))

    i += 1

df = pandas.DataFrame(data_list, columns=['日期', '店铺ID', '渠道', '今日直播场次', '实际合作费用',
                                          '预估佣金费用', '成交金额', '点击量', '支付笔数', '支付件数'])
df.to_excel("D://python导出表格/新媒体营销数据/达人直播/达人直播计划日月年报表==测试用.xlsx", index=False)
