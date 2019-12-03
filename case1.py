# encoding=utf-8
import json
import requests
import selenium
'''反序列化 文件-->字典 json.load()'''

f=open("case1.json","r")#打开文件
f_dict=json.load(f,encoding="utf-8")#文件-->字典
url=f_dict["url"]#字段获取
params=f_dict["params"]
#print(params)
rs=requests.get(url,params=params)#发送请求
print(rs.content)#响应内容
f.close()
f1=open("case2.json","r")
f_dict1=json.load(f1,encoding="utf-8")
url1=f_dict1["url"]
data=f_dict1["data"]
rs1=requests.post(url,data=json.dumps(data))
print rs1.content
