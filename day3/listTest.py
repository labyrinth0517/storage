# 优化：循环 键盘输入一个数字，判断为1那么生成人名，判断为2 那么生成遍数 判断为q or Q 退出
import random
list0 = ["吴承恩", "汉弗莱", "刘醒", "兰尼斯特", "流星花园", "舒克", "汉弗莱1"]
judge1 = 0
judge2 = 0
ran = -1
ran1 = -1
getIN = 0

while getIN != "q" or getIN != "Q":
    print("请输入1或2（重复输入1或2，将更新随机数）：")
    getIN = input()
    if getIN == "1":
        ran = random.randint(0, len(list0) - 1)
        print("已生成处罚人名")
        judge1 = 1
    if getIN == "2":
        ran1 = random.randint(0, 90)
        print("已生成处罚遍数")
        judge2 = 1
    if judge1 == 1 and judge2 == 1:
        print(list0[ran], "处罚了", ran1, "遍")
    if getIN == "q" or getIN == "Q":
        print("正在退出……")
        break
print("end.")
