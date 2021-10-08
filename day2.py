"""
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入  操作完填入：input（“提示”）
3、判断 操作完填入：if判断条件 elif 判断条件……else
4、循环 操作完填入：while 条件循环
任务：
猜3次就结束
"""

import random
import time
counts = 3
answer = random.randint(1, 10)

while counts > 0:
    temp = input("猜一猜数字:)")
    guess = int(temp)
    if temp.isdigit():
        if guess == answer:
            print("答对了")
            break
        else:
            if guess < answer:
                print("小了")
            else:
                print("大了")
        counts = counts - 1
    else:
        print("不要输入其他格式")
        time.sleep(10)
print("end")
