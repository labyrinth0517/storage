# 倒叙打印？
i = 9
j = 1
while i >= 1:
    while j <= i:
        result = i * j
        print(j, "*", i, "=", '%-3d' % result, end="    ")
        j = j + 1
        if j == i+1:
            print()
    i = i - 1
    j = 1
print("end.")
