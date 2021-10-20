# 农业银行
import random
import string

bank = {}
bank_name = '中国农业银行'
bank_option = {1: '开户', 2: '存钱', 3: '取钱', 4: '转账', 5: '查询', 6: 'Bye'}
# 界面


def interface():
    standardIn = '''
*********************************
*      中国农业银行账户管理系统      *
*********************************
*              选项              *
'''
    print(standardIn, end="")
    for i in bank_option.keys():
        print("*          ", i, ":", bank_option[i], "            *")
    print("*********************************")


# 提示输入
def welcome(Inp):
    if Inp in bank_option.keys():
        print('成功选择选项')
    else:
        print('空或不在选项内')


# 判断是否存在
def isExist(choose, options):
    if choose in options:
        return True
    return False


# 随机码
def giveAccount():
    given = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    for i in bank.keys():
        if bank[i]['account'] == given:
            giveAccount()
        else:
            return given


# 获取信息
def getInform(account):
    for i in bank.keys():
        if bank[i]['account'] == account:
            return i
    return None


# 开户
def bank_addUser(username, password, country, province, street, door):
    if username in bank:
        print(2)
    elif len(bank) > 100:
        print(3)
    elif username not in bank:
        bank[username] = {
            'account': giveAccount(),
            'password': password,
            'country': country,
            'province': province,
            'street': street,
            'door': door,
            'money': 0,
            'bank_name': bank_name
        }
        print(1)
        print(bank[username])


# 判断账户、密码是否一致
def judgement(account, password):
    for i in bank.keys():
        if bank[i]['account'] == account and bank[i]['password'] == password:
            return True
        else:
            print('account or password error.')
    return False


# 银行存钱
def saveMoney(account, money):
    bank[getInform(account)]['money'] += money


# 银行取钱
def GetMoney(account, password, money):
    if judgement(account, password) is True:
        if 0 < money <= bank[getInform(account)]['money']:
            bank[getInform(account)]['money'] -= money
        else:
            print('取出金额可能超出余额.')


# 银行查询
def selectUser(account, password):
    if judgement(account, password) is True:
        for i in bank.keys():
            if bank[i]['account'] == account:
                st = str(i)
                print(st, ":", bank[i])
    else:
        print('account or password wrong.')


# 银行转账
def transMoney(account, password, ToAccount):
    for i in bank.keys():
        if bank[i]['account'] == account and bank[i]['password'] == password:
            print('登陆成功，请输入转入账户：')
            if bank[getInform(ToAccount)]['account'] == ToAccount:
                print('找到账户，请输入转入金额：')
                money = int(input())
                bank[i]['money'] += money
                print('success')
        else:
            print('account or password wrong.')


# 主程序
interface()
while True:
    print('请输入您想办理的业务序号>>>')
    Inpt = int(input(''))
    welcome(Inpt)
    if isExist(Inpt, bank_option.keys()):
        if Inpt == 1:
            print('转入开户业务,请输入下列信息：')
            Uname = input('用户名：')
            Pword = input('密码：')
            Countr = input('\t国家：')
            Provin = input('\t省份：')
            Stret = input('\t街道：')
            Dor = input('\t门牌号：')
            bank_addUser(Uname, Pword, Countr, Provin, Stret, Dor)
        if Inpt == 2:
            print('转入存钱业务，请输入下列信息：')
            Ac0 = input('账号：')
            money0 = int(input('存入金额：'))
            saveMoney(Ac0, money0)
        if Inpt == 3:
            print('转入取钱业务，请输入下列信息：')
            Ac1 = input('账号：')
            Ps1 = input('密码：')
            money1 = int(input('金额：'))
            GetMoney(Ac1, Ps1, money1)
        if Inpt == 4:
            print('转入转账业务，请输入下列信息：')
            Ac2 = input('转出账户 账号：')
            Ps2 = input('转出账户 密码：')
            Ac3 = input('转入账户 账号：')
            transMoney(Ac2, Ps2, Ac3)
        if Inpt == 5:
            print('转入查询业务，请输入下列信息：')
            Ac4 = input('账号：')
            Ps4 = input('密码：')
            selectUser(Ac4, Ps4)
        if Inpt == 6:
            print('Bye:)')
            break
