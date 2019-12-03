# coding=utf-8
import smtplib # 用于建立smtp连接
#邮件需要专门的MIME格式
from email.mime.text import MIMEText
from _ast import Sub
from email.mime.multipart import MIMEMultipart #混合MIME格式,支持上次附件
from email.header import Header  # 用于中文邮件主题

# 1. 编写邮件内容（Email邮件需要专门的MIME格式）
msg=MIMEText('this is test email','plain','utf-8') # plain 普通文本格式邮件内容

#2. 组装Email头（发件人，收件人，主题）
msg['To']='lichunhua@aspirecn.com' #发件人
msg['From']='1809731547@qq.com' # 收件人
msg['Subject']='Api Test Report'
msg['pass']='evpadofhcsryegfb'
#3.连接smtp服务器并发送邮件
smtp=smtplib.SMTP() #smtp服务器地址 使用SSL模式
smtp.connect('smtp.qq.com')
smtp.login('1809731547@qq.com',' evpadofhcsryegfb') #自己的邮箱地址和密码
smtp.sendmail(msg.get('From'),msg.get('To'),msg.as_string())#接收邮件地址
smtp.quit()