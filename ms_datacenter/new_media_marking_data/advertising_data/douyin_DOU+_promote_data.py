# 抖音DOU+推广数据

import random
import datetime
import pandas as pd
from faker import Faker
from ms_datacenter.common.login_api import login
from utils.random_HMS import HMS

fake = Faker("zh_CN")

data_list = []


# 设置初始日期
date = datetime.date(2021, 1, 31)

# 设置日期增量
date_increment = datetime.timedelta(days=1)

i = 1

while i <= 2:

    base_list = []

    # 推广类型
    promote_type = 1

    # 视频/内容名称
    session = login.get_session()
    response = session.get("http://14.23.109.84:9092/kolpe/selectScreen?page=1&rows=30&contentId=&title=&isRelease=1")
    title_list = []
    for values in response.json()["data"]["list"]:
        title_list.append(values["title"])

    title = random.choice(title_list)

    # 投放时间
    launch_time = str(date) + " " + HMS.get_hms()

    # 投放时长
    delivery_time = random.randint(2, 12)

    # 投放金额
    delivery_price = random.uniform(0, 50000)

    # 总消耗费用
    douyin_total = random.uniform(0, 50000)

    # 播放量
    play_volume = random.randint(0, 5000000)

    # 点赞量
    likes_volume = random.randint(0, 40000)

    # 评论量
    comment_volume = random.randint(0, 2000)

    # 分享量
    share_volume = random.randint(0, 2500)

    # 主页PV
    homepage_PV = random.randint(0, 1000)

    # 新增粉丝
    fans_new = random.randint(0, 1000)

    # 购物车点击量
    shoppingCart_clicks = random.randint(0, 1000)

    # 备注
    remark_list = ["", fake.paragraph()]
    remark = random.choice(remark_list)

    print("推广类型；%s  视频/内容名称：%s  投放时间：%s  投放时长：%s  投放金额：%.2f  总消费费用：%.2f  播放量：%s  点赞量：%s  "
          "评论量；%s  分享量：%s  主页PV：%s  新增粉丝：%s  购物车点击量：%s  备注：%s" %
          (promote_type, title, launch_time, delivery_time, delivery_price, douyin_total, play_volume, likes_volume,
           comment_volume, share_volume, homepage_PV, fans_new, shoppingCart_clicks, remark))

    base_list.append(promote_type)
    base_list.append(title)
    base_list.append(launch_time)
    base_list.append(delivery_time)
    base_list.append(round(delivery_price, 2))
    base_list.append(round(douyin_total, 2))
    base_list.append(play_volume)
    base_list.append(likes_volume)
    base_list.append(comment_volume)
    base_list.append(share_volume)
    base_list.append(homepage_PV)
    base_list.append(fans_new)
    base_list.append(shoppingCart_clicks)
    base_list.append(remark)

    data_list.append(base_list)

    i += 1


df = pd.DataFrame(data_list, columns=["推广类型（0是私域推广，1是达人推广）", "视频/内容名称", "投放时间", "投放时长", "投放金额",
                                      "总消耗费用", "播放量", "点赞量", "评论量", "分享量", "主页PV", "新增粉丝", "购物车点击量",
                                      "备注"])
df.to_excel("D://python导出表格/新媒体营销数据/广告投放数据/抖音DOU+推广数据==测试用.xlsx", index=False)
