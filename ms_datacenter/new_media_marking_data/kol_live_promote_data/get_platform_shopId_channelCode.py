import random

class PSC:

    @classmethod
    def get_platform_shopId_channelCode(cls):
        list = []
        platform_list = ["天猫", "小红书"]
        platform = random.choice(platform_list)
        list.append(platform)

        if platform == "天猫":
            # 店铺（店铺编码）：colorkey天猫（1CK00001）,superface天猫(1SF00001),瑞沛天猫(1LAB00001)
            shop = ["1CK00001", "1SF00001", "1LAB00001"]
            shop_id = random.choice(shop)
            list.append(shop_id)
        elif platform == "小红书":
            # 店铺（店铺编码）：colorkey小红书2(1CK00005),colorkey抖音旗舰店(1CK00025),superface小红书(1SF00002),瑞沛小红书(1LAB00003)
            shop = ["1CK00005", "1CK00025", "1SF00002", "1LAB00003"]
            shop_id = random.choice(shop)
            list.append(shop_id)

        if platform == "天猫":
            channelCode = "淘宝"
            list.append(channelCode)
        elif platform == "小红书":
            channelCode = "小红书"
            list.append(channelCode)
        return list
