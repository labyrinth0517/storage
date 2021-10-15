# 写一个判断是否为三角形的函数
# parseTriton(a,b,c)
# 参数要求判断边长a,b,c均为1~10的整数
# 返回值：-1（边长不合法），0（非三角形），1（普通三角形），2（等腰三角形），3（等边三角形）
def parsetrigon(a, b, c):
    if a or b or c not in range(1, 11):
        return -1
    else:
        judgement1 = a + b
        judgement2 = a + c
        judgement3 = b + c
        if judgement1 > c and judgement2 > b and judgement3 > a:
            if a == b == c:
                return 3
            if a == b or a == c or b == c:
                return 2
            else:
                return 1


print(parsetrigon(-1, 4, 4))
