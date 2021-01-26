"""
生成随机日期工具

源代码
time1 = (2020,10,1,0,0,0,0,0,0)     # 设置开始时间元组
time2 = (2020,12,1,23,59,59,0,0,0)  # 设置结束时间元组
start_time = time.mktime(time1)     # 生成开始时间戳
end_time = time.mktime(time2)       # 生成结束时间戳

t = random.randint(start_time,end_time) #在开始和结束时间戳中随机取出一个

date_touple =  time.localtime(t)        # 将时间戳生成时间元组
date = time.strftime("%Y-%m-%d",date_touple)

print(date)
"""
import time,random

# 封装调用
class random_date:

    @classmethod
    def get_date(cls,start_date,end_date):

        # 判断传入的开始日期长度，不符合日期格式长度则返回报错信息
        if len(start_date) == 10:
            # 将传入的开始日期，对应年月日位置的字符串装入列表date_num中
            date_num = [start_date[0], start_date[1], start_date[2], start_date[3], start_date[5], start_date[6], start_date[8], start_date[9]]
            num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            i = 0
            # 判断date_num列表的所有字符串是否为数字字符串，是的话则进入下一个else分支提取年月日，生成开始时间元组；否的话返回报错信息
            while i <= 7:
                if date_num[i] in num:
                    i += 1
                else:
                    return ("日期输入有误，请校验，格式：2020-01-01")
            if i == 8:
                # 获取开始时间的年
                start_year = start_date[0:4]

                # 获取开始时间的月，判断月份第一个数是不是0，是的话获取0后面的数字，非0则获取全部
                if start_date[5] == "0":
                    start_month = start_date[6]
                else:
                    start_month = start_date[5:7]

                # 获取开始时间的日，判断日期第一个数是不是0，是的话获取0后面的数字，非0则获取全部
                if start_date[8] == "0":
                    start_day = start_date[9]
                else:
                    start_day = start_date[8:10]

            # print(start_year, start_month, start_day)
        else:
            return ("日期输入有误，请校验，格式：2020-01-01")

        ###############################################################################

        # 判断传入的结束日期长度，不符合日期格式长度则返回报错信息
        if len(end_date) == 10:
            # 将传入的结束日期，对应年月日位置的字符串装入列表date_num中
            date_num = [end_date[0], end_date[1], end_date[2], end_date[3], end_date[5], end_date[6], end_date[8], end_date[9]]
            num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            i = 0
            # 判断date_num列表的所有字符串是否为数字字符串，是的话则进入下一个else分支提取年月日，生成开始时间元组；否的话返回报错信息
            while i <= 7:
                if date_num[i] in num:
                    i += 1
                else:
                    return ("日期输入有误，请校验，格式：2020-01-01")
            if i == 8:
                # 获取结束时间的年
                end_year = end_date[0:4]

                # 获取开始时间的月，判断月份第一个数是不是0，是的话获取0后面的数字，非0则获取全部
                if end_date[5] == "0":
                    end_month = end_date[6]
                else:
                    end_month = end_date[5:7]

                # 获取开始时间的日，判断日期第一个数是不是0，是的话获取0后面的数字，非0则获取全部
                if end_date[8] == "0":
                    end_day = end_date[9]
                else:
                    end_day = end_date[8:10]
            # print(start_year, start_month, start_day)
        else:
            return ("日期输入有误，请校验，格式：2020-01-01")


        time1 = (int(start_year),int(start_month),int(start_day),0,0,0,0,0,0)  # 设置开始时间元组
        time2 = (int(end_year),int(end_month),int(end_day),23,59,59,0,0,0)     # 设置结束时间元组
        t1 = time.mktime(time1)    # 生成开始时间戳
        t2 = time.mktime(time2)  # 生成结束时间戳
        t = random.randint(t1,t2)   # 在开始和结束时间戳中随机取出一个
        date_touple = time.localtime(t) #将时间戳生成时间元组
        date = time.strftime("%Y-%m-%d", date_touple)   # 将时间元组转成格式化字符串（2020-12-23）

        return date

# # 直接打印
# date = random_date.creat_random_date('2020-01-01','2020-12-31')
# print(date)
