# 将列表所有元素拼接成字符串返回
class list_to_str:

    @classmethod
    def get_str(cls,incomming_list):
        i = 0
        list_str = ""
        while i < len(incomming_list) - 1:
            list_str = list_str + incomming_list[i] + "，"
            i += 1
        list_str += incomming_list[i]
        return list_str
