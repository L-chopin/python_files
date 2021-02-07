import requests
from ms_datacenter.common.login_api import login

# 输入用户名和密码，调用Login的get_token方法获取token
token = login.get_token(username="admin",password="123456")

# 构造请求头
headers = {
    "token":token
}
response = requests.get("http://14.23.109.84:9092/brandChannel/findPageByType?page=1&rows=30&type=2",headers=headers)

print("状态码：",response.status_code)
print("响应体：",response.text)

i = 0
while i <= 9:
    print("响应值：",response.json()["data"]["list"][i])
    i += 1