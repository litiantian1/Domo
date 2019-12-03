# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 1. 编写邮件内容
with open('result.html') as f: #打开html报告
    email_bady=f.read() #读取报告内容

msg=MIMEMultipart() #混合MIME格式
msg.attach(MIMEText(email_bady,'html','utf-8')) # 添加html格式邮件内容

# 2.组装Email头（发件人、收件人、主题)
msg['To']='lichunhua@aspirecn.com' #发件人
msg['From']='1809731547@qq.com' # 收件人
msg['Subject']=Header('接口测试报告添加附件','utf-8') #中文邮件主题

# 3.构建附件1，传送当前目录下的test.txt文件
att1=MIMEText(open('result.html','rb').read(),'base64','utf-8') #二进制格式打开文件
att1['Content-Type']='application/octet-stream'
att1["Content-Disposition"]='attachment;filename="result.html"' #filename 为邮件中的附件名
msg.attach(att1) # 添加附件

# 4. 连接smtp服务器并发送邮件
smtp=smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login('1809731547@qq.com','evpadofhcsryegfb') #自己的邮箱地址和密码
smtp.sendmail(msg.get('From'),msg.get('To'),msg.as_string())#接收邮件地址
smtp.quit()