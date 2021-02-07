# 达人直播计划

import random
import datetime
import pandas as pd

# 设置初始日期
date_time = datetime.date(2020, 11, 1)

# 设置日期增量
date_delta = datetime.timedelta(days=1)

i = 1
data_list = []
while i <= 3:                                   # 数据量
    base_list = []

    # 日期
    if i != 1:
        date_time = date_time + date_delta

    # 店铺ID
    shop_id = "1CK00001"

    # 渠道
    channel = "淘宝"

    # 优惠券名称
    coupon_name = ""

    # 机构名称
    mechanism_name = ""

    # 达人名称
    kol_name = ""

    # 账号ID
    account_id = "1515080521"

    # 淘宝客ID
    taoke_ID = ""

    # 今日直播场次
    live_today = ""

    # 实际合作费用
    a = random.uniform(1,1000)

    # 预估佣金比率
    commission_rate = "25"

    # 成交金额（定向计划）


    # 成交金额（优惠券）


    # 成交金额


    # 点击量


    # 支付笔数


    #支付件数


    # 支付买家数


    # 复盘分析


    # 最高在线人数，直播过程中一直看直播的最高人数
    e = random.randint(1000,10000)

    # 观看人数，所有进入该场直播的人数
    d = random.randint(e,int(1.5*e))

    # 平均在线人数
    f = random.randint(int(e/2),int(e*3/4))

    # 稳定在线人数
    c = random.randint(f,e)

    # 抽奖期间在线人数
    b = random.randint(c,e)

    # 新增加购人数
    g = random.randint(0,f)

    print("实际合作费用%f 抽奖期间在线人数%d 稳定在线人数%d 观看人数%d 最高在线人数%d 平均在线人数%d 新增加购人数%d" % (a,b,c,d,e,f,g))


    base_list.append(date_time)
    base_list.append(shop_id)
    base_list.append(channel)
    base_list.append(coupon_name)
    base_list.append(mechanism_name)
    base_list.append(kol_name)
    base_list.append(account_id)
    base_list.append(taoke_ID)
    base_list.append(live_today)
    base_list.append(round(a,2))
    base_list.append(b)
    base_list.append(c)
    base_list.append(d)
    base_list.append(e)
    base_list.append(f)
    base_list.append(g)
    data_list.append(base_list)

    i += 1

print(list)
df=pd.DataFrame(list,columns=['日期','店铺ID','渠道','优惠券名称','机构名称','达人名称','账号ID','淘宝客id','今日直播场次','实际合作费用','抽奖期间在线人数','稳定在线人数','观看人数','最高在线人数','平均在线人数','新增加购人数'])   # 将字段和值一一匹配
df.to_excel('D://python导出表格/新媒体营销数据/达人直播/达人直播计划==测试用.xlsx',index=False)  # 将字段和对应值转化成Excel表格
