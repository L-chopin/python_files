import pymysql

# 创建连接
connect = pymysql.Connect(
    host="14.23.109.84",
    port=3306,
    database="ms_datacenter",
    user="root",
    password="Ms77897854",
    charset="utf8"
)

# 创建游标
cursor = connect.cursor()

# 编写sql,提交
sql = "SELECT * FROM `shop_manage` WHERE id LIKE '1CK%'"
cursor.execute(sql)

# 打印结果
rows = cursor.fetchall()
print(list(rows))
print(type(list(rows)))