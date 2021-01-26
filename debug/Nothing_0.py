import json

# 读取data.json
with open("data.json","r",encoding="utf-8") as f:
    data = json.load(f)
    print(data)

data1 = data
with open("data1.json","w",encoding="utf-8") as f:
    json.dump(data1,f,ensure_ascii=False)