from mysql_connect_ClassMethod import Classmethod_DBUtils

# 调用获取连接的工具函数
connect = Classmethod_DBUtils.get_connect()

# 调用获取游标的工具函数
cursor = Classmethod_DBUtils.get_cursor(connect)

# 编写sql语句，并提交
sql = "SELECT * FROM finance_bank_account"
cursor.execute(sql)
print(cursor.fetchall())

# 调用释放资源的工具函数
Classmethod_DBUtils.close_resource(cursor, connect)
