# 输入圆的半径计算周长与面积
print("【输入圆的半径计算周长与面积】")
print("【输入字母结束】")
radius = 1

while radius > 0:
    try:
        print("请输入圆的半径：")
        radius = float(input())
        if radius > 0:
            Perimeter = 2*3.14159*radius
            Area = 3.14159*radius*radius
            print("这个圆的半径是：", radius)
            print("这个圆的周长是：{:.2f}".format(Perimeter))
            print("这个圆的面积是:{:.2f}".format(Area))
        elif radius <= 0:
            print("这似乎不是个圆:)")
    except ValueError as e:
        print("非数字项目,结束")
        break
