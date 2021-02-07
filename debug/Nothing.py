# import json
#
# dict = {
#     "name":"张三",
#     "age":18,
#     "is_man":True,
#     "school":None
# }
#
#
# str = json.dumps(dict)
# print(str)
#
# str2 = '{"name":"张三","age":18,"is_man":true,"school":null}'
# dict2 = json.loads(str2)
# print(dict2)

dict = {
    "name":"张三",
    "age":18,
    "is_man":True,
    "school":None
}

# print(list(dict.keys()))
# print(type(list(dict.keys())))
for i in list(dict.keys()):
    print(i)
    print(type(i))