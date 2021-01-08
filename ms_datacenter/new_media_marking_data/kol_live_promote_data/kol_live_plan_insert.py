import requests
from date_center.login_api import Login
from Utils.randomDataUtils.random_date import random_date
from date_center.new_media_marketing_date.get_platform_shopId_channelCode import PSC
from date_center.new_media_marketing_date.get_mechanism import mechanism

# 输入用户名和密码，调用Login的get_token方法获取token
token = Login.get_token(username ="admin",password="123456")

# 构造请求头
headers = {
    "token":token,
    "Content-Type":"application/json;charset=UTF-8"
}

liveDate = random_date.creat_random_date("2020-10-01","2020-12-01")

# 三要素
json = {
    "liveDate":random_date.creat_random_date("2020-10-01","2020-12-01"),    # 日期
    "platform":PSC.get_platform_shopId_channelCode()[0],                    # 平台
    "shopId":PSC.get_platform_shopId_channelCode()[1],                      # 店铺
    "channelCode":PSC.get_platform_shopId_channelCode()[2],                 # 渠道
    "couponName":None,                                                      #
    "mechanism":mechanism.get_mechanism(),                                  # 机构名称
    "":None,
}
response = requests.post(
    "http://47.113.97.130:8081/kolLivaPlan/insert",
    json=json
)

# 打印结果
print("状态码：",response.status_code)
print("响应体：",response.text)
