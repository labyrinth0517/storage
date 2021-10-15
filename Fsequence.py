# 从第三项开始，每项都等于前两项的和
# 定义方法
def fsequence(lis, length0):
    lis = [0, 1, 1]
    for i in range(3, length0):
        lis.append(lis[i-1] + lis[i-2])
    print(lis)


lis0 = []
fsequence(lis0, 10)
