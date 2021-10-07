# 创建列表
str1 = [["羽绒服", 253.6, 500, 10],
        ["牛仔裤", 86.3, 600, 60],
        ["风衣", 96.8, 335, 43],
        ["皮草", 135.9, 855, 63],
        ["T血", 65.8, 632, 63],
        ["衬衫", 49.3, 562, 120],
        ["牛仔裤", 86.3, 600, 72],
        ["羽绒服", 253.6, 500, 69],
        ["牛仔裤", 86.3, 600, 35],
        ["羽绒服", 253.6, 500, 140],
        ["牛仔裤", 86.3, 600, 90],
        ["皮草", 135.9, 855, 24],
        ["T血", 65.8, 632, 45],
        ["风衣", 96.8, 335, 25],
        ["牛仔裤", 86.3, 600, 60],
        ["T血", 65.8, 632, 129],
        ["羽绒服", 253.6, 500, 10],
        ["风衣", 96.8, 335, 43],
        ["T血", 65.8, 632, 63],
        ["牛仔裤", 86.3, 600, 60],
        ["皮草", 135.9, 855, 63],
        ["风衣", 96.8, 335, 60],
        ["T血", 65.8, 632, 58],
        ["牛仔裤", 86.3, 600, 140],
        ["T血", 65.8, 632, 48],
        ["风衣", 96.8, 335, 43],
        ["皮草", 135.9, 855, 57],
        ["羽绒服", 253.6, 500, 10],
        ["T血", 65.8, 632, 63],
        ["风衣", 96.8, 335, 78]]
CountList = 0
CountRow = 0


def print_by_row():
    countrow = 0

    while countrow < 30:
        print(str1[countrow])
        countrow = countrow + 1


frame = "================================="
print(frame)
print("服装名称，价格/件，库存数量，销售量/每日")
print_by_row()
print(frame)


# 计算总销售额
def salemoneys():
    countlist = 0
    countrow = 0
    salemoney = 0

    while countlist < 30:
        oner = str1[countrow][1] * str1[countrow][3]
        salemoney = salemoney + oner
        countrow = countrow + 1
        countlist = countlist + 1
    print('(1)本月总销售额为：{:.2f}'.format(salemoney))


salemoneys()


# 日均销售数量
def sale_num_perday():
    countlist = 0
    countrow = 0
    num = 0

    while countlist < 30:
        num = num + str1[countrow][3]
        countrow = countrow + 1
        countlist = countlist + 1
    print('(2)日均销售数量为：{:.2f}'.format(num/30))


sale_num_perday()


# 每个种类的月销售量占比
# 总月销售量（不论种类）
saleNum = 0
while CountList < 30:
    saleNum = saleNum + str1[CountRow][3]
    CountRow = CountRow + 1
    CountList = CountList + 1
print("(3)每个种类月销售量占比：")


# 1
# 羽绒服月销售量总数占比
def salenumber1():
    countnum = 0
    countlist = 0
    countrow = 0

    while countlist < 30:
        if str1[countrow][0] == "羽绒服":
            countnum = countnum + str1[countrow][3]
        countrow = countrow + 1
        countlist = countlist + 1
    print('     羽绒服占总月销售量百分比:{:.2%}'.format(countnum/saleNum))


salenumber1()


# 2
# 牛仔裤月销售量总数占比
def salenumber2():
    countnum = 0
    countlist = 0
    countrow = 0

    while countlist < 30:
        if str1[countrow][0] == "牛仔裤":
            countnum = countnum + str1[countrow][3]
        countrow = countrow + 1
        countlist = countlist + 1
    print('     牛仔裤占总月销售量百分比:{:.2%}'.format(countnum/saleNum))


salenumber2()


# 3
# 风衣月销售量总数占比
def salenumber3():
    countnum = 0
    countlist = 0
    countrow = 0

    while countlist < 30:
        if str1[countrow][0] == "风衣":
            countnum = countnum + str1[countrow][3]
        countrow = countrow + 1
        countlist = countlist + 1
    print('     风衣占总月销售量百分比:{:.2%}'.format(countnum/saleNum))


salenumber3()


# 4
# 皮草月销售量总数占比
def salenumber4():
    countnum = 0
    countlist = 0
    countrow = 0

    while countlist < 30:
        if str1[countrow][0] == "皮草":
            countnum = countnum + str1[countrow][3]
        countrow = countrow + 1
        countlist = countlist + 1
    print('     皮草占总月销售量百分比:{:.2%}'.format(countnum/saleNum))


salenumber4()


# 5
# T血月销售量总数占比
def salenumber5():
    countnum = 0
    countlist = 0
    countrow = 0

    while countlist < 30:
        if str1[countrow][0] == "T血":
            countnum = countnum + str1[countrow][3]
        countrow = countrow + 1
        countlist = countlist + 1
    print('     T血占总月销售量百分比:{:.2%}'.format(countnum/saleNum))


salenumber5()


# 6
# 衬衫月销售量总数占比
def salenumber6():
    countnum = 0
    countlist = 0
    countrow = 0

    while countlist < 30:
        if str1[countrow][0] == "衬衫":
            countnum = countnum + str1[countrow][3]
        countrow = countrow + 1
        countlist = countlist + 1
    print('     衬衫占总月销售量百分比:{:.2%}'.format(countnum/saleNum))


salenumber6()
