# 百分制成绩转换为等级制成绩
# 一次性
print("请输入成绩（百分制）：")
try:
    score = int(input())
    if len(str(score)) > 3:
        print("not three digit")
    elif 0 < len(str(score)) <= 3 and score <= 100:
        if score >= 90:
            print("A.")
        elif 90 > score >= 80:
            print("B.")
        elif 80 > score >= 70:
            print("C.")
        elif 70 > score >= 60:
            print("D.")
        elif score < 60:
            print("E.")
    else:
        print("error.")
except ValueError as e:
    print("not integer")
