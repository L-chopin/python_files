# 达人内容推广计划

import random
import datetime
import pinyin
import pandas as pd
from ms_datacenter.basic_data.kol_account import AdAccount
from ms_datacenter.basic_data.shop_manager import Shop
from ms_datacenter.common.login_api import Login
from ms_datacenter.basic_data.product_data import Product
from ms_datacenter.basic_data.kol_account import AdAccount
from faker import Faker
from utils.random_num_and_letters_code import random_code
from utils.random_number_of_data import random_number_of_data
from utils.list_str_concat import list_to_str

fake = Faker("zh_CN")

data_list = []

# 获取达人账号列表，划分抖音渠道、B站渠道和小红书渠道账号
kol_account_list = AdAccount.get_kol_account_list()
douyin_channel_list = []
bilibili_channel_list =[]
red_book_channel_list = []
for i in kol_account_list:
    if i["channelCode"] == "抖音":
        douyin_channel_list.append(i)
    elif i["channelCode"] == "B站":
        bilibili_channel_list.append(i)
    elif i["channelCode"] == "小红书":
        red_book_channel_list.append(i)

# 获取店铺列表，划分天猫平台店铺和小红书平台店铺
shop_list = Shop.get_shop_list()
tmall_shop_list = []
red_book_shop_list = []
for i in shop_list:
    if i["platform"] == "天猫":
        tmall_shop_list.append(i)
    elif i["platform"] == "小红书":
        red_book_shop_list.append(i)

# 获取商品列表，划分各品牌商品
product_list = Product.get_product_list()
colorkey_product_list = []
superface_product_list = []
lab101_product_list = []
for i in product_list:
    if i["brandCode"] == "COLORKEY珂拉琪":
        colorkey_product_list.append(i)
    elif i["brandCode"] == "SUPERFACE秀芭菲":
        superface_product_list.append(i)
    elif i["brandCode"] == "LAB101瑞沛":
        lab101_product_list.append(i)


# 设置初始日期
date = datetime.date(2020, 1, 1)

# 设置日期增量
date_increment = datetime.timedelta(days=1)

i = 1

while i <= 1000:

    bast_list = []

    # 日期
    if i != 1:
        date = date + date_increment

    # 账号ID（必填）
    # account_id = AdAccount.get_ad_account_id()
    account_id = "123456"

    # 机构
    mechanism_list = ["", "个人", "如涵", "麦芽", "OST", "缇苏", "天宇", "南洋电商", "最美妆", "库库联盟", "春夏", "奥爵", "神狼文化",
                      "宸帆", "黑洞", "无悔", "西瓜", "树格", "微辣文化", "星火", "北斗文化", "圆6", "papitube", "达人说", "洋葱", "新和"]
    mechanism = random.choice(mechanism_list)

    # 是否推广商品
    x = random.randint(0, 1)

    if x == 1:
        # 店铺（必填）
        shopName = Shop.get_shop_name()

        # 平台（必填）
        session = login.get_session()
        params = {
            "shopName": shopName
        }
        response = session.get("http://14.23.109.84:9092/shopMange/selectScreen", params=params)
        platform = response.json()["data"]["list"][0]["platform"]

        # 商品ID
        product_id = product.get_product_id()
    else:
        shopName = ""
        platform = ""
        product_id = ""

    # 计划发布日期
    plan_release_date = date

    # 合作方式（必填）
    cooperation_method_list = ["个人", "星图", "合同", "第三方平台"]
    cooperation_method = random.choice(cooperation_method_list)

    # 合作费用
    cooperation_costs = random.uniform(0, 550000)

    # 账号分类Ⅰ

    account_type_list = ["", "二次元", "母婴亲子", "情侣搭档", "美食吃播", "护肤保养", "口红试色",
                         "剧情", "剧情段子", "生活", "VLOG", "生活vlog", "穿搭分享", "好物分享", "好物推荐", "妆容", "妆容分享",
                         "颜值", "颜值达人", "颜值、美妆", "美妆", "美妆垂直", "美妆测评", "美妆剧情", "美妆教程", "美妆种草", "种草", "种草分享",
                         "帅哥种草", "营销", "营销种草", "开箱", "开箱种草", "开箱推荐"]

    account_type_I = random.choice(account_type_list)

    # c
    if account_type_I == "":
        account_type_II = ""
    else:
        account_type_II = random.choice(account_type_list)

    # 账号类型(0.KOL、1.KOC、2.UGC)
    account_type_list = ["", "0", "1", "2"]
    account_type = random.choice(account_type_list)

    # 粉丝总数
    fans_total = random.randint(0, 50000)

    # 粉丝涨幅
    fans_rise = str(round(random.uniform(0, 100), 2)) + "%"

    # 粉丝年龄17以下
    fans_age_less_17 = random.randint(0, fans_total)

    # 粉丝年龄18~24
    fans_age_18_to_24 = random.randint(0, fans_total - fans_age_less_17)

    # 粉丝年龄25~30
    fans_age_25_to_30 = random.randint(0, fans_total - fans_age_less_17 - fans_age_18_to_24)

    # 粉丝年龄31~35
    fans_age_31_to_35 = random.randint(0, fans_total - fans_age_less_17 - fans_age_18_to_24 - fans_age_25_to_30)

    # 粉丝年龄36~40
    fans_age_36_to_40 = random.randint(0, fans_total - fans_age_less_17 - fans_age_18_to_24
                                       - fans_age_25_to_30 - fans_age_31_to_35)

    # 粉丝年龄41+
    fans_age_outnumber_41 = random.randint(0, fans_total - fans_age_less_17 - fans_age_18_to_24 - fans_age_25_to_30
                                           - fans_age_31_to_35 - fans_age_36_to_40)

    # 女性粉丝占比（%）
    proportion_female_fans = random.randint(0, 100)

    # 曾合作美妆品牌
    beauty_brands_list = ["兰蔻", "雅诗兰黛", "资生堂", "克里斯汀·迪奥", "香奈儿", "Sk-II", "欧莱雅", "美宝莲", "佰草集"]
    worked_beauty_brands_list = [
        "", list_to_str.get_str(
            random_number_of_data.get_random_number_of_data(beauty_brands_list)
            )
    ]
    worked_beauty_brands = random.choice(worked_beauty_brands_list)

    # 前5天平均点赞量
    average_likes_five = random.randint(0, 1000)

    # 预估CPM
    estimated_CPM_list = [0, random.uniform(0, 5000)]
    estimated_CPM = random.choice(estimated_CPM_list)

    # 预估点赞量
    estimated_likes = random.randint(0, 2000)

    # 预估评论量
    estimated_comments = random.randint(0, 2000)

    # 预估成交金额
    estimated_transaction_amount = random.uniform(0, 5000)

    # 预估支付笔数
    estimated_payment = random.randint(0, 100)

    # 授权时长列表
    auth_time_list = ["", "30", "60", "90", "180", "365", "999999"]

    # 是否授权信息流（0不授权，1授权）（必填）
    information_flow_is_auth = random.randint(0, 1)

    if information_flow_is_auth == 1:
        # 信息流授权费用
        information_flow_auth_fee = random.uniform(1, 40000)

        # 信息流授权时长（天/天999999为永久）
        information_flow_auth_time = random.choice(auth_time_list)
    else:
        information_flow_auth_fee = 0
        information_flow_auth_time = ""

    # 是否授权内容热推（0不授权，1授权）（必填）
    hot_push_is_auth = random.randint(0, 1)

    if hot_push_is_auth == 1:
        # 内容热推授权费用
        hot_push_auth_fee = random.uniform(1, 30000)

        # 内容热推授权时长（天/天999999为永久）
        hot_push_auth_time = random.choice(auth_time_list)
    else:
        hot_push_auth_fee = 0
        hot_push_auth_time = ""

    # 是否授权全平台（0不授权，1授权）（必填）
    full_platform_is_auth = random.randint(0, 1)

    if full_platform_is_auth == 1:
        # 全平台授权费用
        full_platform_auth_fee = random.uniform(1, 25000)

        # 全平台授权时长（天/天999999为永久）
        full_platform_auth_time = random.choice(auth_time_list)
    else:
        full_platform_auth_fee = 0
        full_platform_auth_time = ""

    # 是否授权分发微淘（0不授权，1授权）（必填）
    distribution_weitao_is_auth = random.randint(0, 1)

    if distribution_weitao_is_auth == 1:
        # 分发微淘授权费用
        distribution_weitao_auth_fee = random.uniform(1, 10000)

        # 分发微淘授权时长（天/天999999为永久）
        distribution_weitao_auth_time = random.choice(auth_time_list)
    else:
        distribution_weitao_auth_fee = 0
        distribution_weitao_auth_time = ""

    # 联系人
    contacts_list = ["", fake.name()]
    contacts = random.choice(contacts_list)

    if contacts == "":
        # 手机号
        mobile_no = ""
        # 微信号
        wechat = ""
        # 收件人
        recipient = ""
        # 收件地址
        receiving_address = ""
        # 寄样费用
        send_fee = 0
        # 寄样渠道
        send_channel = ""
    else:
        # 手机号
        mobile_no_list = ["", fake.phone_number()]
        mobile_no = random.choice(mobile_no_list)

        # 微信号
        wechat_list = [contacts]
        wechat = random.choice(wechat_list)
        if wechat != "":
            wechat = pinyin.get(wechat, format='strip')

        # 收件人
        recipient = contacts

        # 收件地址
        receiving_address = fake.address()

        # 寄样费用
        send_fee_list = [0, random.uniform(1, 100)]
        send_fee = random.choice(send_fee_list)

        # 寄样渠道
        send_channel_list = ["", "海运", "陆运", "空运"]
        send_channel = random.choice(send_channel_list)

    # 是否发布（0未发布，1发布）（必填）
    is_realse = random.randint(0, 1)

    if is_realse == 1:
        # 视频/内容名称
        title = fake.paragraph()

        # 视频/内容链接
        url = "https://v.douyin.com/" + random_code.get_code(7) + "/"

        # 发布日期
        release_date = date

        # 曝光量
        exposure = random.randint(0, 700000)

        # 播放量
        play_volume = random.randint(0, 20000)

        # 浏览量
        page_view = random.randint(0, 20000)

        # 点赞量
        likes_volume = random.randint(0, 20000)

        # 评论量
        comment_volume = random.randint(0, 20000)

        # 分享量
        share_volume = random.randint(0, 20000)

        # 收藏量
        collection_volume = random.randint(0, 20000)

        # 弹幕量
        barrage_volume = random.randint(0, 20000)

        # 实际成交金额
        actual_gvm = random.uniform(1, 1000)

        # 报备（0为否，1为是）
        report = random.randint(0, 1)

        # 笔记内容类型
        note_type = fake.word()
    else:
        # 视频/内容名称
        title = ""

        # 视频/内容链接
        url = ""

        # 发布日期
        release_date = ""

        # 曝光量
        exposure = ""

        # 播放量
        play_volume = ""

        # 浏览量
        page_view = ""

        # 点赞量
        likes_volume = ""

        # 评论量
        comment_volume = ""

        # 分享量
        share_volume = ""

        # 收藏量
        collection_volume = ""

        # 弹幕量
        barrage_volume = ""

        # 实际成交金额
        actual_gvm = 0

        # 报备（0为否，1为是）
        report = ""

        # 笔记内容类型
        note_type = ""

    # 负责人
    person_charge = fake.name()

    print("%s 账号ID:%s  机构：%s  平台：%s  店铺：%s  商品ID:%s  计划发布日期：%s  合作方式：%s  合作费用：%.2f  账号分类Ⅰ：%s  "
          "账号分类Ⅰ:%s  账号类型：%s  粉丝总数：%s  粉丝涨幅：%s  粉丝年龄17以下：%s  粉丝年龄18~24：%s  粉丝年龄25~30：%s  "
          "粉丝年龄31~35：%s  粉丝年龄36~40：%s  粉丝年龄41+：%s  女性粉丝占比：%.2f  曾合作美妆品牌：%s  前5天平均点赞量：%s  "
          "预估CPM：%.2f  预估点赞量：%s  预估评论量：%s  预估成交金额：%.2f  预估支付笔数：%s  是否授权信息流：%s  信息流授权费用：%.2f  "
          "信息流授权时长：%s  是否授权内容热推：%s  内容热推授权费用：%.2f  内容热推授权时长：%s  是否授权全平台：%s  全平台授权费用：%.2f  "
          "全平台授权时长：%s  是否授权分发微淘：%s  分发微淘授权费用：%.2f  分发微淘授权时长：%s  联系人：%s  微信号：%s  收件人：%s  "
          "手机号：%s 收件地址；%s  寄样费用：%.2f  寄样渠道：%s  是否发布：%s  视频/内容名称：%s  视频/内容链接：%s  发布日期：%s  "
          "曝光量：%s  播放量：%s  浏览量：%s  点赞量：%s  评论量：%s  分享量：%s  收藏量：%s  弹幕量：%s  实际成交金额：%.2f  报备：%s  "
          "笔记内容类型：%s  负责人：%s" %
          (i, account_id, mechanism, platform, shopName, product_id, plan_release_date, cooperation_method,
           cooperation_costs, account_type_I, account_type_II, account_type, fans_total, fans_rise, fans_age_less_17,
           fans_age_18_to_24, fans_age_25_to_30, fans_age_31_to_35, fans_age_36_to_40, fans_age_outnumber_41,
           proportion_female_fans, worked_beauty_brands, average_likes_five, estimated_CPM, estimated_likes,
           estimated_comments, estimated_transaction_amount, estimated_payment, information_flow_is_auth,
           information_flow_auth_fee, information_flow_auth_time, hot_push_is_auth, hot_push_auth_fee,
           hot_push_auth_time, full_platform_is_auth, full_platform_auth_fee, full_platform_auth_time,
           distribution_weitao_is_auth, distribution_weitao_auth_fee, distribution_weitao_auth_time, contacts, wechat,
           recipient, mobile_no, receiving_address, send_fee, send_channel, is_realse, title, url, release_date,
           exposure, play_volume, page_view, likes_volume, comment_volume, share_volume, collection_volume,
           barrage_volume, actual_gvm, report, note_type, person_charge))

    bast_list.append(account_id)
    bast_list.append(mechanism)
    bast_list.append(platform)
    bast_list.append(shopName)
    bast_list.append(product_id)
    bast_list.append(plan_release_date)
    bast_list.append(cooperation_method)
    if cooperation_costs == 0:
        bast_list.append("")
    else:
        bast_list.append(round(cooperation_costs, 2))
    bast_list.append(account_type_I)
    bast_list.append(account_type_II)
    bast_list.append(account_type)
    bast_list.append(fans_total)
    bast_list.append(fans_rise)
    bast_list.append(fans_age_less_17)
    bast_list.append(fans_age_18_to_24)
    bast_list.append(fans_age_25_to_30)
    bast_list.append(fans_age_31_to_35)
    bast_list.append(fans_age_36_to_40)
    bast_list.append(fans_age_outnumber_41)
    if proportion_female_fans == 0:
        bast_list.append("")
    else:
        bast_list.append(round(proportion_female_fans, 2))
    bast_list.append(worked_beauty_brands)
    bast_list.append(average_likes_five)
    if estimated_CPM == 0:
        bast_list.append("")
    else:
        bast_list.append(round(estimated_CPM, 2))
    bast_list.append(estimated_likes)
    bast_list.append(estimated_comments)
    if estimated_transaction_amount == 0:
        bast_list.append("")
    else:
        bast_list.append(round(estimated_transaction_amount, 2))
    bast_list.append(estimated_payment)
    bast_list.append(information_flow_is_auth)
    if information_flow_auth_fee == 0:
        bast_list.append("")
    else:
        bast_list.append(round(information_flow_auth_fee, 2))
    bast_list.append(information_flow_auth_time)
    bast_list.append(hot_push_is_auth)
    if hot_push_auth_fee == 0:
        bast_list.append("")
    else:
        bast_list.append(round(hot_push_auth_fee, 2))
    bast_list.append(hot_push_auth_time)
    bast_list.append(full_platform_is_auth)
    if full_platform_auth_fee == 0:
        bast_list.append("")
    else:
        bast_list.append(round(full_platform_auth_fee, 2))
    bast_list.append(full_platform_auth_time)
    bast_list.append(distribution_weitao_is_auth)
    if distribution_weitao_auth_fee == 0:
        bast_list.append("")
    else:
        bast_list.append(round(distribution_weitao_auth_fee, 2))
    bast_list.append(distribution_weitao_auth_time)
    bast_list.append(contacts)
    bast_list.append(wechat)
    bast_list.append(recipient)
    bast_list.append(mobile_no)
    bast_list.append(receiving_address)
    if send_fee == 0:
        bast_list.append("")
    else:
        bast_list.append(round(send_fee, 2))
    bast_list.append(send_channel)
    bast_list.append(is_realse)
    bast_list.append(title)
    bast_list.append(url)
    bast_list.append(release_date)
    bast_list.append(exposure)
    bast_list.append(play_volume)
    bast_list.append(page_view)
    bast_list.append(likes_volume)
    bast_list.append(comment_volume)
    bast_list.append(share_volume)
    bast_list.append(collection_volume)
    bast_list.append(barrage_volume)
    if actual_gvm == 0:
        bast_list.append("")
    else:
        bast_list.append(round(actual_gvm, 2))
    bast_list.append(report)
    bast_list.append(note_type)
    bast_list.append(person_charge)

    data_list.append(bast_list)

    i += 1

df = pd.DataFrame(data_list, columns=["账号ID", "机构", "平台", "店铺", "商品ID", "计划发布日期", "合作方式", "合作费用", "账号分类Ⅰ",
                                      "账号分类Ⅱ", "账号类型", "粉丝总数", "粉丝涨幅", "粉丝年龄17以下", "粉丝年龄18~24",
                                      "粉丝年龄25~30", "粉丝年龄31~35", "粉丝年龄35~40", "粉丝年龄41+", "女性粉丝占比", "曾合作美妆品牌",
                                      "前5天平均点赞量", "预估CPM", "预估点赞量", "预估评论量", "预估成交金额", "预估支付笔数",
                                      "是否授权信息流（0不授权，1授权）", "信息流授权费用", "信息流授权时长（天/999999为永久）",
                                      "是否授权内容热推（0不授权，1授权）", "内容热推授权费用", "内容热推授权时长（天/999999为永久）",
                                      "是否授权全平台（0不授权，1授权）", "全平台授权费用", "全平台授权时长（天/999999为永久）",
                                      "是否授权分发微淘（0不授权，1授权）", "分发微淘授权费用", "分发微淘授权时长（天/999999为永久）",
                                      "联系人", "微信号", "收件人", "手机号","收件地址", "寄样费用", "寄样渠道", "是否发布（0未发布，1发布）",
                                      "视频/内容名称", "视频/内容链接", "发布日期", "曝光量", "播放量", "浏览量", "点赞量", "评论量",
                                      "分享量", "收藏量", "弹幕量", "实际成交金额", "报备（0为否，1为是）", "笔记内容类型", "负责人"])
df.to_excel("D://python导出表格/新媒体营销数据/达人内容推广数据/推广计划数据==测试用.xlsx", index=False)
