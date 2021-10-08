# leap Year闰年判断
# 一次性
print("请输入一个年份(不超过四位数)：")
year = str(input())
if len(year) <= 4 and int(year) > 0:
    year = int(year)
    if year % 4 == 0:
        print("这年是闰年XD")
    if year % 4 != 0:
        print("这年不是闰年:(")
else:
    print("超过四位数或为负数")
