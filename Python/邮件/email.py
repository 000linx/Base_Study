from datetime import timedelta
import random
import smtplib
from flask import Flask,session
from email.mime.text import MIMEText
from email.header import Header

# QQ邮箱的SMTP服务器地址
smtp_server = 'smtp.qq.com'
# QQ邮箱的SMTP服务器端口
smtp_port = 465

# 发件人邮箱账号和授权码
sender_email = '1405128011@qq.com'
sender_password = 'rkguaemrwsijbafa'

# 收件人邮箱账号
receiver_email = '1395468221@qq.com'


vertify_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])

# 邮件内容
subject = '你好张皓翔同学'
body = f'你正在尝试修改您的学生服务密码请确认是你本人操作，验证码为{vertify_code}'

# 创建MIMEText对象
message = MIMEText(body, 'plain', 'utf-8')

# 设置邮件头部
message['From'] = f"{Header('StudentServices', 'utf-8')} <{sender_email}>"
message['To'] = receiver_email
message['Subject'] = Header(subject, 'utf-8')

try:
    # 连接到SMTP服务器
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    # 登录到SMTP服务器
    server.login(sender_email, sender_password)
    # 发送邮件
    server.sendmail(sender_email, [receiver_email], message.as_string())
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    # 关闭连接
    if 'server' in locals():
        server.quit()