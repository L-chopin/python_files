# 商品优惠券数据汇总

import random
import datetime

data_list = []

i = 1

while i <= 3:
    # 店铺
    shop = 0

    # 平台
    plat_form = 0

    # 渠道
    channel = 0

    # 推广类型
    promote_type = 0

    # 优惠券名称
    coupon_name = 0

    # 商品ID
    product_no = 0

    # 开始时间
    start_time = 0

    # 日期增量
    time_delta = datetime.timedelta(days=7)

    # 结束时间
    end_time = start_time + time_delta

    # 发行张数
    circulation = 0

    # 状态
    state = 0



    x = random.uniform(1.00,8.99)   # 商品单价
    b = random.randint(1,1000)      # 优惠券发行张数/有效期 = 日发行张数
    c = random.randint(int(b/2),b)  # 使用张数
    d = random.randint(c-50,c+50)   # 支付件数
    e = int(d*2/3)                  # 支付买家数
    a = x*d                         # 成交金额
    print("%.2f    %d    %d    %d    %d" % (a,b,c,d,e))
    i += 1