# 有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
def trans2dic(list):    # 必须传入二维列表，一维存在报错可能
    dic0 = {}
    for i in range(len(list)):
        dic0.update({list[i][0]: list[i][1:]})
    print(dic0)


names = [
    ["刘备", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700, "10"]
]
trans2dic(names)
