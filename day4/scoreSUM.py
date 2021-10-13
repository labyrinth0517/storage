list0 = [
    ["罗恩", 23, 35, 44],
    ["哈利", 60, 77, 68, 88, 90],
    ["赫敏", 97, 99, 89, 91, 95, 90],
    ["马尔福", 100, 85, 90]
]

for i in range(len(list0)):
    sum0 = 0
    for j in range(1, len(list0[i])):
        sum0 = sum0 + list0[i][j]
    print(list0[i][0], sum0)
