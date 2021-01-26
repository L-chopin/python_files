"""
    需求：访问银行账户查询接口
    流程：三要素
    1.根据url定位接口资源
    2.提交测试数据
    3.发送请求，接受并处理响应结果
"""

# 导包
import requests

from Utils.connect_utils.mysql_connect_ClassMethod import DBUtils

# 三要素
connect = DBUtils.get_connect()
cursor = connect.cursor()
sql = "SELECT id FROM finance_bank_account WHERE account_name = '林晓彬'"
cursor.execute(sql)
id = cursor.fetchone()[0]
DBUtils.close_resource(cursor,connect)
json = {
    "id": id,
    "accountName": "林晓彬",
    "bankAccount": "654321",
    "openAccountBank": "农业银行"
}
response = requests.post(
    "http://47.113.97.130:8081/dist/index.html#/financial/update",
    json = json
)

# 打印结果
print("状态码：",response.status_code)
print("响应体：",response.text)
