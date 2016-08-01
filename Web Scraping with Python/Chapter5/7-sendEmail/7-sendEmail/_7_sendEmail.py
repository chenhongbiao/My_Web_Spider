#import smtplib
#from email.mime.text import MIMEText

#msg = MIMEText("The body of the mail is here")
#msg['Subject'] = "An Email Alert"
#msg["From"] = "faustmeow@163.com"
#msg["To"] = "fautmeow@162.com"

#s = smtplib.SMTP("localhost")
#s.send_message(msg)
#s.quit()

#163.com - email server
#servername serverIP              SSL port   non-SSL port
#SMTP            smtp.163.com  465/994    25
#
#coding:utf-8
import smtplib  
from email.mime.text import MIMEText  # 引入smtplib和MIMEText

host = 'smtp.163.com'  # 设置发件服务器地址
port = 25  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
sender = 'faustmeow@163.com'  # 设置发件邮箱，一定要自己注册的邮箱
pwd = 'xxxxxxx'  # 设置发件邮箱的密码，等会登陆会用到
receiver = '798696497@qq.com' # 设置邮件接收人，这里是我的公司邮箱
body = '<h1>What your name</h1><p>Hello Meow! How are you?</p>' # 设置邮件正文，这里是支持HTML的
#body = 'Hello Meow!'

msg = MIMEText(body, 'html') # 设置正文为符合邮件格式的HTML内容
msg['subject'] = 'Hello world' # 设置邮件标题
msg['from'] = sender  # 设置发送人
msg['to'] = receiver  # 设置接收人

s = smtplib.SMTP(host, port)  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
s.login(sender, pwd)  # 登陆邮箱
s.sendmail(sender, receiver, msg.as_string())  # 发送邮件！

print ("successful!")  # 发送成功就会提示

#因为没有附件，所以代码部分很简单，如果带了附件，推荐下Envelope，
#描述里说是Mailing for human beings(模仿requests)