import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(server_host: str, server_port: int, sender: str, receiver, password: str, code: str):
    html = ""
    with open("email.html", "r", encoding="utf-8") as f:
        html = f.read()
    send_email(server_host, server_port, sender, receiver, "【AuthME】您的邮箱验证码", html.replace("{code}", code),
               password)


def send_email(server_host: str, server_port: int, sender: str, receiver, subject, message, password: str):
    # 创建一个SMTP对象，连接到SMTP服务器
    smtp = smtplib.SMTP(server_host, server_port)
    # 启动TLS加密
    # smtp.starttls()
    # 登录到SMTP服务器，使用发件人的邮箱和密码
    smtp.login(sender, password)
    # 创建一个MIMEMultipart对象，用于包含邮件内容
    msg = MIMEMultipart()
    # 设置发件人，收件人和主题
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    # 创建一个MIMEText对象，用于存放HTML消息
    html = MIMEText(message, 'html')
    # 将HTML消息附加到MIMEMultipart对象中
    msg.attach(html)
    # 将邮件内容转换为字符串
    content = msg.as_string()
    # 发送邮件，使用发件人，收件人和邮件内容
    smtp.sendmail(sender, receiver, content)
    # 关闭SMTP连接
    smtp.quit()
