import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.163.com"
mail_user = "15927478077"
mail_pass = "hjb123456"

sender = '15927478077@163.com'
receivers = ['15927478077@163.com']

message = MIMEText('Python邮件测试', 'plain', 'utf-8')
message['From'] = Header("bin", "utf-8")
message['To'] = Header("测试", "utf-8")

subject = '你好呀'
message['Subject'] = Header(subject, "utf-8")

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Erro: 无法发送")

