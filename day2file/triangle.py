# 输入三条边长，如果能构成三角形就计算周长和面积
print("输入三条边长，构成三角形，计算周长与面积")
print("请依次输入三角形三边：")
print("（边长请均为正方向的整数，不支持向量计算）")
try:
    length1 = int(input("三角形的第一条边长："))
    length2 = int(input("三角形的第二条边长："))
    length3 = int(input("三角形的第三条边长："))
    if length1 > 0 and length2 > 0 and length3 > 0:
        print("===至少三边均大于零===")
        judgement1 = length1 + length2
        judgement2 = length1 + length3
        judgement3 = length2 + length3
        if judgement1 > length3 and judgement2 > length2 and judgement3 > length1:
            print("这三边似乎能构成三角形:)")
        else:
            print("这三边似乎不能构成三角形:(")
    else:
        print("也许有任意一边小于或等于零:(")
except ValueError as e:
    print("error.not integer.")
