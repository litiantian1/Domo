# encoding=utf-8
import requests
import json

'''文件的序列化与序列化'''
#1.序列化：字典->文件句柄
#字典格式
res_dict = {'name': '张三', 'password': '123456', "male": True, "money": None}
#f=open('demo1.JSON',"w") #新增文件demo2.json
#json.dump(res_dict,f) #字典内容保存为文件

#2. 反序列化：文件句柄-->字典

f2=open("demo2.JSON","r")#读文件
print f2
f2_dict=json.load(f2,encoding="utf-8")#将文件句柄转化成为字典
print f2_dict
print(f2_dict['name'])#读取其中的参数
f2.close()
