# 对列表进行冒泡排序
a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(a)
