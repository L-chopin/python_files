# 传进来列表或者字典，删除随机个数（至少保留一个），再返回
import random


class random_number_of_data:

    @classmethod
    def get_random_number_of_data(cls,incoming_box):

        if  type(incoming_box) == list:
            n = random.randint(1,len(incoming_box)-1)
            for i in range(n):
                x = random.choice(incoming_box)
                incoming_box.remove(x)
            return incoming_box

        elif type(incoming_box) == dict:
            keys = list(incoming_box.keys())
            n = random.randint(1,len(incoming_box)-1)
            for i in range(n):
                x = random.choice(keys)
                keys.remove(x)
                del incoming_box[x]

            return incoming_box
