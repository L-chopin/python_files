"""
    需求：访问银行账户查询接口
    流程：三要素
    1.根据url定位接口资源
    2.提交测试数据
    3.发送请求，接受并处理响应结果
"""

# 导包
import requests

from ms_datacenter.common.login_api import login

# 输入用户名和密码，调用Login的get_token方法获取token
token = login.get_token()

# 构造请求头
headers = {
    "token":token
}

# 访问银行账户查询接口，并接收响应
response = requests.get("http://14.23.109.84:9092/financeba/selectScreen",headers = headers)

# 打印结果
print("状态码：",response.status_code)
print("响应体：",response.text)
