# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
username = "root"
userP = "admin"
counts = 3

while True:
    userNin = str(input('请输入用户名：'))
    userPin = str(input('请输入密码：'))
    if userNin == username and userP == userPin:
        print("登陆成功:)")
        break
    else:
        counts = counts - 1
        if counts > 0:
            print("错误，请重新输入。")
            print("(", counts, "/3)")
        if counts == 0:
            print("错误三次，锁定")
            break
print("end.")
