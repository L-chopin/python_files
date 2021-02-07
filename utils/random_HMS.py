# 随机时分秒
# 2016-12-10 7:06:29 codegay
import random
st = "07:30:00"
et = "19:30:00"
class HMS:

    @classmethod
    def time2seconds(cls,t):
        h,m,s = t.strip().split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)

    @classmethod
    def seconds2time(cls,sec):
        m,s = divmod(sec,60)
        h,m = divmod(m,60)
        return "%02d:%02d:%02d" % (h,m,s)

    @classmethod
    def get_hms(cls):

        sts = HMS.time2seconds(st)
        # sts==27000
        ets = HMS.time2seconds(et)
        # ets==34233
        rt = random.sample(range(sts,ets),1)
        # rt == [28931, 29977, 33207, 33082, 31174, 30200, 27458, 27434, 33367, 30450]

        # rt.sort()
        # 对时间从小到大排序

        for r in rt:
            return str(HMS.seconds2time(r))
