import random,datetime
import pandas as pd
from utils.random_num_and_letters_code import random_code

data_list = []

# 设置初始日期
date_time = datetime.date(2021, 1, 1)

# 设置日期增量
date_delta = datetime.timedelta(days=1)

z = 1
# 数据量
while z <= 1:

    base_list = []

    KOL_list = ['薇娅','李佳琦','辛有志','罗永浩','张沫凡','林允','雪梨','林依轮','张大奕','徐冬冬']

    order_distribution_resources_list = ["精华","面霜","乳液","洗面奶","面膜","隔离霜","气垫bb","粉底液","唇釉","美妆蛋","眼线笔","定妆喷雾","小金块","小银管"]

    # 计划ID
    plan_ID = 'xiaobing1'

    # 日期
    if z != 1:
        date_time = date_time + date_delta

    # 视频链接
    video_link = "www.%s.com" % random_code.get_code(8)

    # 投放达人
    KOL = random.choice(KOL_list)

    # 采买CPM数量
    buy_CPM_number = random.randint(0,15)

    # 消耗费用
    consumption_cost = random.uniform(100,3000)

    # 随单配送资源
    order_distribution_resources = random.choice(order_distribution_resources_list)

    # 曝光量
    exposure = random.randint(500,40000)

    # 点击量
    click_number = random.randint(10,20000)

    # 转化数
    transformation_number = random.randint(10,3000)

    # 点赞量
    likes = random.randint(10,40000)

    # 评论量
    comments = random.randint(10,20000)

    # 转发量
    forwarding_volume = random.randint(10,45000)

    # 收藏量
    collection_volume = random.randint(10,40000)

    # 落地页PV
    landing_page_PV = random.randint(100,50000)

    # 落地页UV
    landing_page_UV = random.randint(50,landing_page_PV)

    # 商品单价
    price = random.uniform(8.00,29.99)

    # 支付笔数
    payments_number = random.randint(1,100)

    # 支付件数
    pay_number = payments_number * random.randint(1,5)

    # 成交金额
    gvm = price*pay_number

    # 播放量
    play_number = random.randint(50,25000)

    # 有效播放量
    effective_play_number = random.randint(10,play_number)

    # 25 % 进度播放量
    twenty_five_play_number = random.randint(0,play_number)

    # 50 % 进度播放量
    fifty_play_number = random.randint(0,play_number - twenty_five_play_number)

    # 75 % 进度播放量
    seventy_five_play_number = random.randint(0,play_number - twenty_five_play_number - fifty_play_number)

    # 99 % 进度播放量
    ninety_nine_play_number = random.randint(0,play_number - twenty_five_play_number - fifty_play_number - seventy_five_play_number)

    # 平均单次播放时长，单位（秒）
    average_play_time = str(random.randint(0,30))

    # 话题播放次数
    topic_play_times = random.randint(10,15000)

    # 流量分成进度（ % ）
    flow_share_pace = str(random.randint(0,100)) + "%"

    # 活动分享数
    activity_share_number = random.randint(50,15000)

    # 私信数
    private_letter_number = random.randint(50,10000)

    # 主页访问量
    homepage_visit_number = random.randint(50,15000)

    base_list.append(date_time)
    base_list.append(plan_ID)
    base_list.append(video_link)
    base_list.append(KOL)
    base_list.append(buy_CPM_number)
    base_list.append(round(consumption_cost,2))
    base_list.append(order_distribution_resources)
    base_list.append(exposure)
    base_list.append(click_number)
    base_list.append(transformation_number)
    base_list.append(likes)
    base_list.append(comments)
    base_list.append(forwarding_volume)
    base_list.append(collection_volume)
    base_list.append(landing_page_PV)
    base_list.append(landing_page_UV)
    base_list.append(payments_number)
    base_list.append(pay_number)
    base_list.append(round(gvm,2))
    base_list.append(play_number)
    base_list.append(effective_play_number)
    base_list.append(twenty_five_play_number)
    base_list.append(fifty_play_number)
    base_list.append(seventy_five_play_number)
    base_list.append(ninety_nine_play_number)
    base_list.append(average_play_time)
    base_list.append(topic_play_times)
    base_list.append(flow_share_pace)
    base_list.append(activity_share_number)
    base_list.append(private_letter_number)
    base_list.append(homepage_visit_number)

    data_list.append(base_list)


    print(
        "日期：%s  计划ID：%s  视频链接：%s  投放达人：%s  采买cpm数量：%s  消耗费用：%s  随单配送资源：%s  曝光量：%s  点击量：%s  "
        "转化数：%s  点赞量：%s  评论量：%s  转发量：%s  收藏量：%s  落地页PV：%s  落地页UV：%s  支付笔数：%s  支付件数：%s  成交金额：%s  "
        "播放量：%d  有效播放量：%d  25%%进度播放量：%d  50%%进度播放量：%d  75%%进度播放量：%d  99%%进度播放量：%d  平均单次播放时长：%s  "
        "话题播放次数：%d  流量分成进度：%s  活动分享数：%d  私信数：%d  主页访问量：%d" %
        (date_time, plan_ID, video_link, KOL, buy_CPM_number, round(consumption_cost,2), order_distribution_resources,exposure,
         click_number, transformation_number, likes, comments, forwarding_volume, collection_volume, landing_page_PV,
         landing_page_UV, payments_number, pay_number, round(gvm,2),play_number,effective_play_number,twenty_five_play_number,
         fifty_play_number,seventy_five_play_number,ninety_nine_play_number,average_play_time,topic_play_times,
         flow_share_pace,activity_share_number,private_letter_number,homepage_visit_number)
    )
    z += 1
3


# 将字段和值一一匹配
df=pd.DataFrame(data_list,columns=['日期','计划ID','视频链接','投放达人','采买cpm数量','消耗费用','随单配送资源','曝光量','点击量','转化数',
                                   '点赞量','评论量','转发量','收藏量','落地页PV','落地页UV','支付笔数','支付件数','成交金额','播放量','有效播放量',
                                   '25%进度播放量','50%进度播放量','75%进度播放量','99%进度播放量','平均单次播放时长','话题播放次数','流量分成进度',
                                   '活动分享数','私信数','主页访问量'])

# 将字段和对应值转化成Excel表格
df.to_excel('D://python导出表格/新媒体营销数据/广告投放数据/广告投放计划日报表==测试用新.xlsx',index=False)