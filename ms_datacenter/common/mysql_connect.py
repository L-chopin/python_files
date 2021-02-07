"""
 实现封装：
    将pymysql的常见用法实现封装
    连接数据中台测试库
"""
import pymysql

class DBUtils:

    # 工具函数：1.获取连接
    def get_connect(self):
        return pymysql.connect(
            host="14.23.109.84",
            port=3306,
            database="ms_datacenter",
            user="root",
            password="Ms77897854",
            charset="utf8"
        )

    # 工具函数：2.获取游标
    def get_cursor(self,connect):
        return connect.cursor

    # 工具函数：3.释放资源
    def close_resource(self,cursor,connect):
        if cursor:
            cursor.close()
        if connect:
            connect.close()