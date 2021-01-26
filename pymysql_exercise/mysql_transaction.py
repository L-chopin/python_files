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

# 4.核心操作-事务
try:
    # 4.1编写sql语句，并执行，提交
    sql1 = "UPDATE finance_bank_account SET bank_account = '4424' WHERE account_name = '林晓彬'"
    sql2= "DELETE FROM finance_bank_account WHERE account_name = '林晓彬'"

    # 执行sql语句
    cursor.execute(sql1)
    cursor.execute(sql2)

    # 提交
    connect.commit()

except Exception as error:
    # 4.2回滚，抛出异常
    connect.rollback()
    print("error:",error)

# 5.释放资源（关闭游标，关闭连接）
cursor.close()
connect.close()
