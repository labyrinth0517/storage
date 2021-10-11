# 使用+、-调换两个数的值
#一次性
import keyboard

num0 = 56
num1 = 78
temp = 0

print("试调换两个数的值")
print("只验证功能，不提供手动输入实验数据")
print("已知：")
print("A：", num0)
print("B：", num1)
while True:
    try:
        if keyboard.is_pressed('+') or keyboard.is_pressed('-'):
            temp = num0
            num0 = num1
            num1 = temp
            print("按下按键:)")
            print("展示两个数的值：")
            print("A：", num0)
            print("B：", num1)
            break
        else:
            pass
    except ValueError as e:
        print("error")
        break
