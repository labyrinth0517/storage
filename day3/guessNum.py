# 猜数字-循环-三次-三次结束
import random

counts = 3
answer = random.randint(1,10)

while counts > 0:
    temp = input("猜数字：")
    guess = int(temp)

    if guess == answer:
        print("对了")
        break
    else:
        if guess < answer:
            print("小了")
        if guess > answer:
            print("大了")
    counts = counts - 1
print("end.")