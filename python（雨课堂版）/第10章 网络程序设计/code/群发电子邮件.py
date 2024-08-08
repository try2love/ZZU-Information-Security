import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
import smtplib

sender = '你的电子邮件地址'
username = '你的用户名'
userpwd = '你的电子邮箱密码'

# 这里以126邮箱为例，可以根据需要进行修改
host = 'smtp.126.com'
port = 25

body = '''这是《Python程序设计开发宝典》和《Python可以这样学》的作者董付国发来的测试信息。'''

# 要群发的电子邮件地址
recipients = ('第一个收件人电子邮件地址',
              '第二个收件人电子邮件地址',
              '第三个收件人电子邮件地址')

# 登录邮箱服务器
server = smtplib.SMTP(host, port)
server.starttls()
server.login(username, userpwd)
# 开始群发
for recipient in recipients:
    # 创建邮件
    msg = MIMEMultipart()
    msg.set_charset('utf-8')
    # 回复地址与发信地址可以不同
    # 但是大部分邮件系统在回复时会提示
    msg['Reply-to'] = '你的另外一个电子邮件地址'
    # 设置发信人、收信人和主题
    msg.add_header('From', sender)
    msg.add_header('To', recipient)
    msg.add_header('Subject', '这是一个测试')
    # 设置邮件文字内容
    msg.attach(MIMEText(body, 'plain',_charset="utf-8"))
    
    # 添加图片
    with open('测试图片.jpg', 'rb') as fp:
        msg.attach(MIMEImage(fp.read()))

    # 添加附件文件
    attachment = MIMEBase('text', 'txt')
    with open('测试附件.txt', 'rb') as fp:
        attachment.set_payload(fp.read())
    email.encoders.encode_base64(attachment)
    attachment.add_header('content-disposition',\
                          'attachment',filename=('utf-8', '', '测试附件.txt'))
    msg.attach(attachment)
    
    # 发送邮件
    server.send_message(msg)
    
server.quit()
