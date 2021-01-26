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
    host="47.113.97.130",
    port=3306,
    database="ms_datacenter",
    user="root",
    password="123456",
    charset="utf8"
)

# 3.创建游标
cursor = connect.cursor()

# 4.核心操作：发送sql语句
# 4.1编写sql语句
sql = "UPDATE finance_bank_account SET bank_account = '4424' WHERE account_name = '林晓彬'"
# 4.2执行sql
cursor.execute(sql)
connect.commit()
# 4.3获取响应结果
# 4.3.1获取响应结果行数
print("受影响行数：",cursor.rowcount)

# 5.释放资源（关闭游标，关闭连接）
cursor.close()
connect.close()
