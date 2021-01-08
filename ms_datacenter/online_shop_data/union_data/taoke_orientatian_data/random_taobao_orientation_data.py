# 定向计划明细随机生成

import random,datetime
import pandas as pd


# 设置初始日期
date_time = datetime.date(2020, 12, 28)

# 设置日期增量
date_delta = datetime.timedelta(days=1)

# 设置初始数据列表
data_list = []

i = 1
while i <= 1:

    base_list = []

    # 日期
    if i != 1:
        date_time = date_time + date_delta

    # 店铺
    shop = "colorkey天猫"

    # 渠道
    channel = "抖音KOL"

    # 淘宝客PID
    taoke_pid = "654321"

    # 计划名称
    plan_name = "大兵计划"

    # 佣金率
    x = random.uniform(0.30,0.32)

    # 商品单价
    y = random.uniform(20,80)

    # 点击量
    clicks = random.randint(0,1200)

    # 支付笔数
    pay_nums = random.randint(0,int(clicks/3))

    # 成交金额
    gvm = y*pay_nums

    # 确认收货金额
    receipt_amount = random.uniform(0,gvm/3)

    # 佣金费用
    commission = receipt_amount*x

    base_list.append(date_time)
    base_list.append(shop)
    base_list.append(channel)
    base_list.append(taoke_pid)
    base_list.append(plan_name)
    base_list.append(round(commission,2))
    base_list.append(round(receipt_amount,2))
    base_list.append(clicks)
    base_list.append(round(gvm,2))
    base_list.append(pay_nums)


    data_list.append(base_list)


    print("佣金费用%.2f 确认收货金额%.2f 点击量%d 成交金额%.2f 支付笔数%d" % (commission,receipt_amount,clicks,gvm,pay_nums))
    i += 1


# 将字段和值一一匹配
df=pd.DataFrame(data_list,columns=['日期','店铺','渠道','淘宝客PID','计划名称','佣金费用','确认收货金额','点击量','成交金额','支付笔数'])

# 将字段和对应值转化成Excel表格
df.to_excel('D://python导出表格/线上店铺数据/联盟数据/淘宝客定向计划明细==测试用.xlsx',index=False)