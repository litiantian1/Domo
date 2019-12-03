# encoding=utf-8
import json
import requests
import re
'''带安全认证的请求 （Cookie/Session/appid/token/sign）'''

#需要登录的请求（Cookie/Session认证）
#1.使用会话保持

#s=requests.session()#新建一个会话

url="https://demo.fastadmin.net/admin/index/login"
'''
s_res=s.get(url).text #使用get方法获取页面token
# print(s_res)
p2 = s_res.find('\"__token__\"')#获取token信息
# print('找到位置：')
# print(p2)
token=s_res[p2+19:p2+51]#截取token
print("token:"+token)
data={"username":"admin","password":"123456","__token__":token,"keeplogin":1}
p_res=s.post(url,data=data)#使用post方法发送登录请求

print(p_res.text)
'''

#2. 通过抓包工具抓取cookie
#PHPSESSID: 42d036547dab1e4ff7f2fedbc3be4930
'''
url1="https://demo.fastadmin.net/admin/index/index"
cookies={"PHPSESSID":"42d036547dab1e4ff7f2fedbc3be4930"}
res=requests.get(url1,cookies=cookies)#携带cookie发送请求
print(res.text)
'''

#3. appid或者token 方式

app_key = 'N2Rzea28gzaqQ0xG4bmwR6xO'
secret_key = 'h6RNF7btM6Q03ZP9ukXWc8461XmZzkTd'
img_url = 'http://upload-images.jianshu.io/upload_images/7575721-40c847532432e852.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
# 获取token
get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(app_key,secret_key)
token = requests.get(url=get_token_url).json().get("access_token")  # 从获取token接口的响应中取得token值
print token
# 识别图片文字
orc_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={}'.format(token)
data = {"url": img_url}
res = requests.post(url=orc_url, data=data)
print(json.dumps(res.json(), indent=2, ensure_ascii=False)) # 格式化输出
