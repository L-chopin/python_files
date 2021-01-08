"""
 实现封装：
    将pymysql的常见用法实现封装
"""
import pymysql

class classmethod_DBUtils:

    # 工具函数：1.获取数据中台测试库连接
    @classmethod
    def get_connect(cls):
        return pymysql.connect(
            host="47.113.97.130",
            port=3306,
            database="ms_datacenter",
            user="root",
            password="123456",
            charset="utf8"
        )

    # 工具函数：2.获取游标
    @classmethod
    def get_cursor(cls,connect):
        return connect.cursor()

    # 工具函数：3.释放资源
    @classmethod
    def close_resource(cls,cursor,connect):
        if cursor:
            cursor.close()
        if connect:
            connect.close()