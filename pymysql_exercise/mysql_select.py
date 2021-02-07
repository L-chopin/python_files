"""
使用pymysql连接数据库，无论增删改查，操作流程基本都一致
1.导包
2.创建连接
3.创建游标
4.核心操作：发送sql语句
5.释放资源（关闭游标，关闭连接）
"""

# 1.导包
import pymysql

# 2.创建连接
connect = pymysql.Connect(
    host="14.23.109.84",
    port=3306,
    database="ms_datacenter",
    user="root",
    password="Ms77897854",
    charset="utf8"
)

# 3.创建游标
cursor = connect.cursor()


# 4.核心操作：发送sql语句
# 4.1编写sql语句
# sql = "SELECT id FROM finance_bank_account WHERE account_name = '林晓彬'"
sql = "SELECT id FROM `taotuan_product_plan_details`"
# 4.2执行sql
cursor.execute(sql)
# 4.3获取响应结果
# 4.3.1获取响应结果行数
print("响应结果行数：",cursor.rowcount)
# 4.3.2逐行获取数据
# row1 = cursor.fetchone()
# row2 = cursor.fetchone()
# row3 = cursor.fetchone()
# row4 = cursor.fetchone()
# row5 = cursor.fetchone()
# row6 = cursor.fetchone()
# row7 = cursor.fetchone()
# row8 = cursor.fetchone()
#
# print(row1)
# print(row2)
# print(row3)
# print(row4)
# print(row5)
# print(row6)
# print(row7)
# print(row8)

# 4.3.3获取所有数据
# rows = cursor.fetchone()[0]
rows = cursor.fetchall()
for i in rows:
    print(i[0])
    print(type(i[0]))
# for row in rows:
#     print("每一条数据：",row)
#     print("id",row[0])
#     print("账户名称",row[1])
#     print("银行账号",row[2])
#     print("开户银行",row[3])
#     print("是否默认",row[4])
# 5.释放资源（关闭游标，关闭连接）
cursor.close()
connect.close()
