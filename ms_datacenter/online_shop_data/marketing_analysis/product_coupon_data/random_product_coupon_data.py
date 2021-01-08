# 商品优惠券明细数据随机生成

import random

i = 1
print("成交金额 领取数量 使用张数 支付件数 支付买家数")
while i <=3:
    x = random.uniform(1.00,8.99)   # 商品单价
    b = random.randint(1,1000)      # 优惠券发行张数/有效期 = 日发行张数
    c = random.randint(int(b/2),b)  # 使用张数
    d = random.randint(c-50,c+50)   # 支付件数
    e = int(d*2/3)                  # 支付买家数
    a = x*d                         # 成交金额
    print("%.2f    %d    %d    %d    %d" % (a,b,c,d,e))
    i += 1
