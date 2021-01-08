# 达人直播商品明细
# from Utils.randomDataUtils.Random_numAndLettersCode import random_code
import random

I = 1

while I <= 4:                       # 数据量
    # A = random_code.creat_randomCode()    # 随机编码
    x = random.uniform(20,40)       # 商品单价
    b = random.randint(250,1500)    # PV:页面浏览量（包含一个用户多次访问的浏览量）
    a = random.randint(150,b)       # UV：独立访客量（浏览页面的所有独立访客量）
    c = random.randint(100,a)       # 下单买家数
    f = random.randint(50,c)        # 支付买家数（去重）
    e = int(f*3/2)                  # 支付件数
    g = random.randint(f,b)         # 商品浏览人数
    h = random.randint(0,c)         # 加购人数
    i = random.randint(f,int(1.5*f))# 支付人数（未去重）
    d = x*e                         # 成交金额
    print("UV %d  PV %d  下单买家数%d 成交金额%.2f 支付件数%d 支付买家数%d 商品浏览人数%d 加购人数%d 支付人数%d" % (a,b,c,d,e,f,g,h,i))
    I += 1