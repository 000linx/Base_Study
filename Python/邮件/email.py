import smtplib
from email.mime.text import MIMEText
from email.header import Header

# QQ邮箱的SMTP服务器地址
smtp_server = 'smtp.qq.com'
# QQ邮箱的SMTP服务器端口
smtp_port = 465

# 发件人邮箱账号和授权码
sender_email = 'test@qq.com'
sender_password = '授权码'

# 收件人邮箱账号
receiver_email = 'test@qq.com'

# 邮件内容
subject = '你好马露斌同学'
body = '你正在尝试修改您的学生服务密码请确认是你本人'

# 创建MIMEText对象
message = MIMEText(body, 'plain', 'utf-8')

# 设置邮件头部
message['From'] = f"{Header('Sender Name', 'utf-8')} <{sender_email}>"
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