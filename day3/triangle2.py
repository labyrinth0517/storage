# 输入三条边长，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
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
            print("尝试判断属于什么三角形")
            judgement4 = length1 * length1
            judgement5 = length2 * length2
            judgement6 = length3 * length3
            j4 = judgement5 + judgement6
            j5 = judgement4 + judgement6
            j6 = judgement4 + judgement5
            if length1 == length2 or length1 == length3 or length2 == length3:
                print("可能是等腰三角形:|")
            elif length1 == length2 == length3:
                print("可能是等边三角形:|")
            elif judgement4 == j4 or judgement5 == j5 or judgement6 == j6:
                print("可能是直角三角形:|")
            else:
                print("可能是普通三角形:)")
        else:
            print("这三边似乎不能构成三角形:(")
    else:
        print("也许有任意一边小于或等于零:(")
except ValueError as e:
    print("error.not integer.")
