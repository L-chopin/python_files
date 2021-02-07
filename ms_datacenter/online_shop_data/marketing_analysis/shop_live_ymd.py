# 店铺直播日月年报表

import random
import datetime
import pandas as pd


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

    # 店铺ID
    shop_id_list = ["1CK00001", "1SF00001", "1LAB00001", "1CK00005", "1CK00025", "1LAB00003", "1SF00002"]
    shop_id = "1CK00001"
    # shop_id = random.choice(shop_id_list)

    # 直播场次
    live_num = random.randint(1, 10)

    # 观看量
    watch_num = random.randint(100, 15000)

    # 新增粉丝量
    new_add_funs = random.randint(0, watch_num)

    # 商品点击量
    goods_clicks = random.randint(0, 2000)

    # 支付笔数
    pay_number = random.randint(1, goods_clicks)

    # 单价
    price = random.uniform(8.9, 29.9)

    # 成交金额
    transaction_amount = pay_number*price

    # 成功退款金额
    refund_money = transaction_amount*random.uniform(0, 0.15)

    # 支付件数
    pay_num = random.randint(0, 400)

    # 引导加购数
    guide_buy_back_num = random.randint(0, 1200)

    # 引导加购人数
    guide_buy_back_people = random.randint(0, 300)

    # 引导支付子订单数据
    guide_pay_sub_order_num = random.randint(0, 400)

    # 引导进店人数
    guide_enter_people_num = random.randint(0, 400)

    # 引导进店量
    guide_enter_num = random.randint(0, 6000)

    # 引导支付人数
    guide_pay_people_num = random.randint(0, guide_enter_num)

    # 定向计划点击量
    orientation_plan_clicks = random.randint(0, 5000)

    # 定向计划支付笔数
    orientation_plan_pay_number = random.randint(0, orientation_plan_clicks)

    # 定向计划成交金额
    orientation_plan_transaction_amount = orientation_plan_pay_number * price

    # 淘宝客支付笔数
    tbk_pay_number = random.randint(0, 100)

    # 淘宝客付款预估收入
    tbk_income_payment = random.uniform(1, 200)

    # 打赏音浪
    reward_soundbyte = random.randint(0, 200)

    # 总消耗费用
    consumption_cost_count = random.uniform(0, 15000)

    # 打赏金额
    reward_amount = random.randint(0, 100)

    # 直播间订单量（即时影响）
    live_room_order_num_now = random.randint(0, 300)

    # 直播间订单量（长效影响-7天）
    live_room_order_num_week = random.randint(0, 200)

    # 直播间成交金额（即时影响）
    live_room_deal_amount_now = live_room_order_num_now * price

    # 直播间成交金额（长效影响-7天）
    live_room_deal_amount_week = live_room_order_num_week * price

    print("店铺ID：%s  日期：%s  直播场次：%s  观看量：%d  新增粉丝量：%d  商品点击量：%d  支付笔数：%d  成交金额：%.2f成功退款金额：%.2f  "
          "支付件数：%d  引导加购数：%d  引导加购人数：%d  引导支付子订单数据：%d  引导进店人数：%d  引导进店量：%d  引导支付人数：%d  定向计划点击量：%d  "
          "定向计划支付笔数：%d  定向计划成交金额：%.2f  淘宝客支付笔数：%d  淘宝客付款预估收入：%.2f  打赏音浪：%d  总消耗费用：%.2f  "
          "打赏金额：%.2f  直播间订单量（即时影响）:%d  直播间订单量（长效影响-7天）：%d  直播间成交金额（即时影响）：%d  直播间成交金额（长效影响-7天）：%.2f" %
          (shop_id, date_time, live_num, watch_num, new_add_funs, goods_clicks, pay_number, transaction_amount,
           refund_money, pay_num, guide_buy_back_num, guide_buy_back_people, guide_pay_sub_order_num,
           guide_enter_people_num, guide_enter_num, guide_pay_people_num, orientation_plan_clicks,
           orientation_plan_pay_number, orientation_plan_transaction_amount, tbk_pay_number, tbk_income_payment,
           reward_soundbyte, consumption_cost_count, reward_amount, live_room_order_num_now, live_room_order_num_week,
           live_room_deal_amount_now, live_room_deal_amount_week))

    base_list.append(shop_id)
    base_list.append(date_time)
    base_list.append(live_num)
    base_list.append(watch_num)
    base_list.append(new_add_funs)
    base_list.append(goods_clicks)
    base_list.append(pay_number)
    base_list.append(round(transaction_amount, 2))
    base_list.append(round(refund_money, 2))
    base_list.append(pay_num)
    base_list.append(guide_buy_back_num)
    base_list.append(guide_buy_back_people)
    base_list.append(guide_pay_sub_order_num)
    base_list.append(guide_enter_people_num)
    base_list.append(guide_enter_num)
    base_list.append(guide_pay_people_num)
    base_list.append(orientation_plan_clicks)
    base_list.append(orientation_plan_pay_number)
    base_list.append(round(orientation_plan_transaction_amount, 2))
    base_list.append(tbk_pay_number)
    base_list.append(round(tbk_income_payment, 2))
    base_list.append(reward_soundbyte)
    base_list.append(round(consumption_cost_count, 2))
    base_list.append(round(reward_amount, 2))
    base_list.append(live_room_order_num_now)
    base_list.append(live_room_order_num_week)
    base_list.append(round(live_room_deal_amount_now, 2))
    base_list.append(round(live_room_deal_amount_week, 2))

    data_list.append(base_list)

    i += 1

df = pd.DataFrame(data_list, columns=["店铺ID", "日期", "直播场次", "观看量", "新增粉丝量", "商品点击量", "支付笔数", "成交金额", "成功退款金额",
                                      "支付件数", "引导加购数", "引导加购人数", "引导支付子订单数据", "引导进店人数", "引导进店量", "引导支付人数",
                                      "定向计划点击量", "定向计划支付笔数", "定向计划成交金额", "淘宝客支付笔数", "淘宝客付款预估收入", "打赏音浪",
                                      "总消耗费用", "打赏金额", "直播间订单量（即时影响）", "直播间订单量（长效影响-7天）", "直播间成交金额（即时影响）",
                                      "直播间成交金额（长效影响-7天）"])

df.to_excel('D://python导出表格/线上店铺数据/营销分析/店铺直播日月年报表==测试用.xlsx', index=False)
