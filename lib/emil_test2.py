# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.config import *

def send_email(report_file):
    msg=MIMEMultipart() # 混合MIME格式
    msg.attach(MIMEText(open(report_file).read(),'html','utf-8')) # 添加html格式的邮件正文，会丢失css格式

    # 2.组装Email头（发件人、收件人、主题)
    msg['To'] = 'lichunhua@aspirecn.com'  # 发件人
    msg['From'] = '1809731547@qq.com'  # 收件人
    msg['Subject'] = Header(subject, 'utf-8')  # 中文邮件主题，从配置文件中读取

    # 3.构建附件1，传送当前目录下的test.txt文件
    att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开文件
    att1['Content-Type'] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment;filename="test.txt"'  # filename 为邮件中的附件名
    msg.attach(att1)  # 添加附件

    try:
        smtp=smtplib.SMTP(smtp_server)#从配置文件中读取
        smtp.login(smtp_user,smtp_password) #自己的邮箱地址和密码,从配置文件中读取
        smtp.sendmail(msg.get('From'),msg.get('To'),msg.as_string())#接收邮件地址
        logging.info("邮件发送成功2019！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
