# 第一题
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]
]

sum0 = 0
ages = 0
count1 = 0
count2 = 0

# 每个人的平均薪资：
for i in range(4):
    sum0 = names[i][5] + sum0
print("平均薪资：", sum0 / 4)

# 每个人的平均年龄：
for i in range(4):
    ages = int(names[i][1]) + ages
print("平均年龄：", ages / 4)

# 公司新来一个员工，【刘备，45，男，220，alibaba，500,30】，添加到列表中
names.append(["刘备", "45", "男", "220", "alibaba", 500, "30"])
print(names)

# 统计公司男女人数
for i in range(len(names)):
    if names[i][2] == "男":
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print("男：", count1, "女:", count2)

# 每个部门的人数
bumenlist0 = []
bumenlist1 = []
for j in range(5):
    if names[j][6] not in bumenlist0:
        bumenlist0.append(names[j][6])
print(bumenlist0)
for i in range(4):
    for j in range(5):
        count3 = 0
        if bumenlist0[i] == names[j][6]:
            count3 = count3 + 1
            bumenlist1.append(count3)
print(bumenlist1)
