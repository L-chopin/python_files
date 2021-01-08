# 达人直播计划小红书平台店铺计划分日明细
import random
# import pandas as pd
i = 1
list = []
while i <=2:                        # 数据量
    base_list = []
    x = random.uniform(1.00,8.99)   # 商品单价
    b = random.randint(1,1000)      # 优惠券发行张数/有效期 = 日发行张数
    c = random.randint(int(b/2),b)  # 使用张数
    d = random.randint(c-50,c+50)   # 支付件数
    e = int(d*2/3)                  # 支付买家数
    a = x*d                         # 成交金额
    print("成交金额%.2f 支付件数%d 支付买家数%d" % (a,d,e))
    # base_list.append(a)
    # base_list.append(d)
    # base_list.append(e)
    # list.append(base_list)
    i += 1

# print(list)
# df=pd.DataFrame(list,columns=['成交金额','支付件数','支付买家数'])   # 将字段和值一一对应
# df.to_excel('计划分日明细.xlsx',index=False)                      # 将字段和对应值转化成Excel表格