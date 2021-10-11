# 输入10个数字，并打印10个数的求和结果
# i是从0开始取值的
print("请输入10个数字：")
num = [0]*10
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
    print(sumN)
