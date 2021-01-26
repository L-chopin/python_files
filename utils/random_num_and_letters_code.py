# 随机生成任何位数，任何形式【数字和大小写字母混合，纯数字，纯小写字母，纯大写字母，纯字母（含大小写）】编码
import random

# 封装调用
class random_code:

    # 数字大小写字母混合编码
    @classmethod
    def get_code(cls,number_of_code):
        num = ["1","2","3","4","5","6","7","8","9","0"]

        capital_letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                          "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        lowercase_letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                            "n","o","p","q","r","s","t","u","v","w","x","y","z"]

        randomList = [num,capital_letter,lowercase_letter]

        n = 1
        while n <= 1:        # 需要生成的编码个数
            i = 1
            code = ""
            while i <= number_of_code:    # 需要生成的编码的位数
                x = random.choice(randomList)
                y = random.choice(x)
                code += y
                i += 1
            return code
            n += 1

    # 纯数字编码
    @classmethod
    def get_num_code(cls,number_of_code):
        num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        n = 1
        while n <= 1:  # 需要生成的编码个数
            i = 1
            code = "0"
            while i <= number_of_code:  # 需要生成的编码的位数
                x = random.choice(num)
                code += x
                i += 1
            return code
            n += 1

    # 纯小写字母编码
    @classmethod
    def get_capital_letter_code(cls,number_of_code):
        lowercase_letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                            "n","o","p","q","r","s","t","u","v","w","x","y","z"]
        n = 1
        while n <= 1:  # 需要生成的编码个数
            i = 1
            code = ""
            while i <= number_of_code:  # 需要生成的编码的位数
                x = random.choice(lowercase_letter)
                code += x
                i += 1
            return code
            n += 1

    # 纯大写字母编码
    @classmethod
    def get_lowercase_letter_code(cls,number_of_code):
        capital_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        n = 1
        while n <= 1:  # 需要生成的编码个数
            i = 1
            code = ""
            while i <= number_of_code:  # 需要生成的编码的位数
                x = random.choice(capital_letter)
                code += x
                i += 1
            return code
            n += 1

    # 随机大小写字母编码
    @classmethod
    def get_letters_code(cls,number_of_code):
        capital_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        lowercase_letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        randomList = [capital_letter,lowercase_letter]

        n = 1
        while n <= 1:        # 需要生成的编码个数
            i = 1
            code = ""
            while i <= number_of_code:    # 需要生成的编码的位数
                x = random.choice(randomList)
                y = random.choice(x)
                code += y
                i += 1
            return code
            n += 1



# # 直接打印
# code = random_code.get_random_letters()
# print(code)
