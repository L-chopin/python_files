"""
    需求：访问银行账户新增接口
    流程：三要素
    1.根据url定位接口资源
    2.提交测试数据
    3.发送请求，接受并处理响应结果
"""

# 导包
import requests

# 三要素
data = {"accountName":"林晓彬","bankAccount":"123456","openAccountBank":"农业银行"}
response = requests.post(
    "http://47.113.97.130:8081/dist/index.html#/financial/add",
    data=data
)

# 打印结果
print("状态码：",response.status_code)
print("响应体：",response.text)
