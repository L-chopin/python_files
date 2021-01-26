import json

dict = {
    "name":"张三",
    "age":18,
    "is_man":True,
    "school":None
}


str = json.dumps(dict)
print(str)

str2 = '{"name":"张三","age":18,"is_man":true,"school":null}'
dict2 = json.loads(str2)
print(dict2)