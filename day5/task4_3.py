# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
def list2dic(list):
    listbuf = []
    dic0 = {}
    for j in range(len(list)):
        if list[j] not in listbuf:
            listbuf.append(list[j])
            dic0.update({list[j]: 1})
        elif list[j] in listbuf:
            dic0[list[j]] = dic0[list[j]] + 1
    print(dic0)


lis1 = [21, 21, 21, 56, 56, 56, 56, 56, 56, 56, 56, 56, 10, 10, 10]
list2dic(lis1)
