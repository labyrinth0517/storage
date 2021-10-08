# 英寸转换厘米
print("【英寸转换厘米】")
print("请输入英寸或厘米，以in或cm为结尾：")
str0 = str(input())
judgeStr01 = "in"
judgeStr02 = "cm"
while str0[-2:] == judgeStr01 or judgeStr02:
    if str0[-2:] == "in":
        centimeter = float(str0[:-2])*2.54
        print(str0, "转换厘米是：{:.2f}".format(centimeter), "cm")
    if str0[-2:] == "cm":
        inch = float(str0[:-2])/2.54
        print(str0, "转换为英寸是：{:.2f}".format(inch), "in")
    print("请输入英寸或厘米，以in或cm为结尾：")
    str0 = str(input())
    if str0[-2:] != judgeStr02 and judgeStr01:
        break
print("end")
