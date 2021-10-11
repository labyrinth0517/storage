# 用循环实现20以内的阶乘
result = 0
times = 1

for i in range(1, 21):
    for j in range(1, i+1):
        times = times * j
    result = result + times
    for x in range(1, i+1):
        if x == i:
            print(x, "!", end="")
        else:
            print(x, "!+", end=" ")
    print("=", result)
    times = 1
print("end.")
