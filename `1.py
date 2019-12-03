# coding=utf-8
import smtplib # 用于建立smtp连接
#邮件需要专门的MIME格式
from email.mime.text import MIMEText
from _ast import Sub

mail_to_list = ["xxxxx@aisino.com", "xxxx@aisino.com", "xxxx@qq.com"]

mail_host = "smtp.qq.com"
mail_user = "1809731547"
mail_pass = "evpadofhcsryegfb"#（授权码是服务商提供163的来自163提供（这个自己填写），qq的由qq提供（这个qq发给你）
mail_postfix = "qq.com"


# 发送邮件
def send_mail(to_list, sub, content):
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.login(mail_user, mail_pass)
    s.sendmail(me, to_list, msg.as_string())
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
    except smtplib.SMTPException as error:
        print(error)
    finally:
        s.close()


if __name__ == "__main__":
    send_mail('lichunhua@aspirecn.com', "系统测试2217", "test")