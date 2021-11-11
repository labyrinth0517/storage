# log日志查看，记录ip地址出现次数
wk = open(file='baidu_x_system.log', encoding='utf-8')
# 使用变量声明
ManiData = ''
dataDic = {}

count = len(wk.readlines())  # 获取文件总行数
wk.seek(0)  # 读文件指针重置
for j in range(count):
    ManiData = ''
    buf1line = wk.readline()
    for i in buf1line:
        if i == ' ':
            break
        else:
            ManiData += i
    if ManiData not in dataDic:
        dataDic.update({ManiData: 1})
    elif ManiData in dataDic:
        dataDic[ManiData] += 1
print(dataDic)
