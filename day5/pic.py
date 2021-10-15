def startower(length):
    count0 = 10
    for i in range(1, length):
        count0 = count0 - 1
        print(" " * count0, end="")
        for j in range(1, i+1):
            print("* ", end="")
        print()
    print("end.")

startower(10)   # 生成底层“*”为length-1，高度为length-1的星星塔