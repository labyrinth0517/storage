dic0 = {
    "苹果": 32.8,
    "香蕉": 22,
    "葡萄": 15.5
    }
# 根据水果名称查询购买这个水果的费用
print("请输入水果名称以查询这个水果的费用(苹果、香蕉、葡萄)：")
name = str(input())
for i in dic0.keys():
    if name == i:
        print(i, ":", dic0[i])


Friuts = {
        "苹果": 12.3,  # 水果和单价
        "草莓": 4.5,
        "香蕉": 6.3,
        "葡萄": 5.8,
        "橘子": 6.4,
        "樱桃": 15.8
        }
info = {
    '小明': {
            'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
            'money': {}
            },
    '小刚': {
            'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
            'money': {}
            }
}

# 小明
money = 0
for i in Friuts.keys():
    for j in info["小明"]["fruits"].keys():
        if i == j:
            money = Friuts[i] * info["小明"]["fruits"][j]
            info["小明"]["money"][i] = money
print("小明：", info["小明"]["money"])
sum0 = 0
for i in info["小明"]["money"].values():
    sum0 = i + sum0
print("小明花费总金额：", sum0)

# 小刚
money = 0
for i in Friuts.keys():
    for j in info["小刚"]["fruits"].keys():
        if i == j:
            money = Friuts[i] * info["小刚"]["fruits"][j]
            money = round(money, 3)
            info["小刚"]["money"][i] = money
print("小刚：", info["小刚"]["money"])
sum1 = 0
for i in info["小刚"]["money"].values():
    sum1 = i + sum1
print("小刚花费总金额：", sum1)
