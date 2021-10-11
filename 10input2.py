# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
print("请依次输入10个数，将展示最大的数、10个数的和、与这10个数的平均数")
num = [0]*10
temp = 0
sumN = 0
errorNum = 0

for i in range(len(num)):
    print("请输入第", i+1, "项数字，（", i+1, "/", len(num), ")")
    try:
        num[i] = int(input())
        print(num)
    except ValueError as e:
        print("似乎没有输入数字.end")
        errorNum = 1
        break
if errorNum != 1:
    for i in range(len(num)):
        sumN = sumN + num[i]
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            temp = num[i]
            num[i] = num[i+1]
            num[i+1] = temp
    average = sumN/len(num)
    print("这10个数中最大的数为：", num[-1])
    print("这10个数的和为：", sumN)
    print("这10个数的平均数为：", average)