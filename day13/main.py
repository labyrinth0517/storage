import smtplib
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from HTMLTestRunner import HTMLTestRunner
from email.header import Header


test = unittest.defaultTestLoader.discover(r'D:\Eadd\pycharmStorage\day13', pattern='Test*.py')

runner = HTMLTestRunner.HTMLTestRunner(
    title='计算机测试报告',
    description='测试报告',
    verbosity=1,
    stream=open(file='计算机.html', mode='w+', encoding='utf-8')

)

runner.run(test)

sender = 'sortasky@foxmail.com'
password = 'pwssrbgyclttdghb'
receiver = ['2431320433@qq.com']

msg0 = MIMEMultipart()
msg0['From'] = Header('Huang', 'utf-8')
msg0['To'] = Header('2431320433')
msg0['Subject'] = 'python20-day13'
msg0.attach(MIMEText('见附件', 'plain', 'utf-8'))

msg = MIMEText(open(r'D:\Eadd\pycharmStorage\day13\计算机.html', 'rb').read(), 'base64', 'utf-8')
msg['Content-Type'] = 'application/octet-stream'
msg['Content-Disposition'] = 'attachment;filename="Test.html"'
msg0.attach(msg)

try:
    smt = smtplib.SMTP('smtp.qq.com')
    smt.helo()
    smt.ehlo()
    smt.starttls()
    smt.login(sender, password)
    smt.sendmail(sender, receiver, msg0.as_string())
    smt.quit()
    print('邮件发送成功')
except smtplib.SMTPException:
    print('无法发送邮件')
