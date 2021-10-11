# 打印那个图形
Wp = "* "
count0 = 12

for i in range(1, 8):
    count0 = count0 - 1
    print(" " * count0, end="")
    for j in range(1, i+1):
        print(Wp, end="")
    print()
print("end.")
