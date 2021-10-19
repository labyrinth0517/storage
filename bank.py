# 中国工商银行账户管理系统
import xlwt
import xlrd
import random
from xlutils.copy import copy

xl = xlwt.Workbook()
sheet = xl.add_sheet('account')
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
font.underline = False
font.italic = False
style.font = font


bank = {}
bank_name = '中国银行'
# 获取文件、行数、列数 由于python按行运行，要放在使用前的最后一个位置？
data = xlrd.open_workbook("D:\Eadd\pycharmStorage\day6\estbank.xls")
table = data.sheet_by_name('account')
# rowNum = table.nrows
# colNum = table.ncols


def bank_add(account, username, password, country, province, street, door):
    if username in bank:
        return 2
    elif len(bank) > 100:
        return 3
    else:
        bank[username] = {
            'account': account,
            'password': password,
            'country': country,
            'province': province,
            'street': street,
            'door': door,
            'money': 0,
            'bank_name': bank_name
        }
        return 1


# 用户
class User:
    def create(self):
        account = random.randint(10000000, 99999999)
        username = input('请输入用户名:')
        password = input('请输入密码：')
        print('下面输入您的详细地址：')
        country = input("\t请输入您的国家")
        province = input("\t请输入您的省份")
        street = input("\t请输入您的街道")
        door = input("\t请输入您的门牌号")
        add = bank_add(account, username, password, country, province, street, door)
        if add == 3:
            print('银行已满')
        elif add == 2:
            print('请输入其他用户名')
        elif add == 1:
            print('开户成功')
            info = '''
                       ------------个人信息------------
                       用户名:%s
                       账号：%s
                       密码：*****
                       国籍：%s
                       省份：%s
                       街道：%s
                       门牌号：%s
                       余额：%s
                       开户行名称：%s
                   '''
            # 每个元素都可传入%
            print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))

            count0 = 1
            # if table.cell_value(0, 1) != 'account':
            for i in bank[username].keys():
                if count0 <= len(bank[username]):
                    sheet.write(0, count0, i)
                    count0 = count0 + 1
            sheet.write(table.nrows, 0, username)
            count0 = 1
            for j in bank[username].values():
                if count0 <= len(bank[username]):
                    sheet.write(table.nrows, count0, j)
                    count0 = count0 + 1
            xl.save("D:\Eadd\pycharmStorage\day6\estbank.xls")
            # elif table.cell_value(0, 1) == 'account':
            #     count0 = 1
            #     for j in bank[username].values():
            #         if count0 <= len(bank[username]):
            #             sheet.write(table.nrows, count0, j)


print("***************************")
print("*    中国银行账户管理系统    *")
print("***************************")
print("*          1、开户         *")
print("*          2、存钱         *")
print("*          3、取钱         *")
print("*          4、转账         *")
print("*          5、查询         *")
print("*          6、再见         *")
print("***************************")
# 功能逻辑
u = User()
print("请输入操作：")
chose = int(input())
if chose == 1:
    User.create(u)
elif chose == 2:
    print("请输入用户名与密码")
    username0 = input("用户名：")
    password0 = input('密码：')
    rb = xlrd.open_workbook('estbank.xls')
    wb = copy(rb)
    ws = wb.get_sheet(0)
    if username0 == sheet.cell(1, 1).value and password0 == sheet.cell(1, 2).value:
        savemoney = int(input('请输入存入款项：'))
        ws.write(1, 7, savemoney)
elif chose == 3:
    print("请输入用户名与密码")
    username0 = input("用户名：")
    password0 = input('密码：')
    rb = xlrd.open_workbook('estbank.xls')
    wb = copy(rb)
    ws = wb.get_sheet(0)
    if username0 == sheet.cell(1, 1).value and password0 == sheet.cell(1, 2).value:
        getmoney = int(input('请输入取款金额：'))
        if getmoney <= sheet.cell(1, 7).value:
            sa = sheet.cell(1, 7).value - getmoney
            ws.write(1, 7, sa)
        else:
            print('没那么多钱')
elif chose == 4:
    print("请输入转入账户的用户名")
    username0 = input("用户名：")
    rb = xlrd.open_workbook('estbank.xls')
    wb = copy(rb)
    ws = wb.get_sheet(0)
    if username0 == sheet.cell(1, 1).value:
        print('请输入转入款项：')
        money0 = int(input())
        a = sheet.cell(1, 7).value
        ws.write(1, 7, a + money0)
elif chose == 5:
    print("请输入用户名与密码")
    username0 = input("用户名：")
    password0 = input('密码：')
    rb = xlrd.open_workbook('estbank.xls')
    wb = copy(rb)
    ws = wb.get_sheet(0)
    if username0 == sheet.cell(1, 1).value and password0 == sheet.cell(1, 2).value:
        showmoney = sheet.cell(1, 7).value
        print('您的余额为：', showmoney)
elif chose == 6:
    print('已退出，欢迎下次再见')
