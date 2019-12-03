# encoding=utf-8
import requests
import json

#JSON类型解析
'''JSON格式操作方法：序列化与放序列化'''

data={
    'name':'张三',
    'password':'123456',
    'male':True,
    "money":None
}#字典格式
str_data=json.dumps(data) #序列化，（字典->文本/文本句柄）,转化成合适的Json文本，方便HTTP传输

url="http://www.tuling123.com/openapi/api"
params={"key":"ec961279f453459b9248f0aeb6600bbe","info":"怎么又是你"}
res = requests.post(url,params=params)
print(res.text) # 输出为一行文本
res_dict=res.json()#将响应转化为json对象，等同于'json.loads(res.text)'
print(res_dict)
#序列化（字典->文本/文本句柄）：json.dumps/dump
res_txt=json.dumps(res_dict,indent=2,sort_keys=True,ensure_ascii=False)#重新转化成文本
#indent:缩进空格数，indent=0 输出为一行；sort_keys=True:将json结果按ascii码排序；ensure_ascii=False:如果返回格式为utf-8包含中文，不转化为\u...
print(res_txt)

#反序列化（文本/文件句柄->字典）：json.loads()/json.load()
#json文本格式的响应信息
res_text = {"name": "张三", "password": "123456"}
print type(res_text)
#res_dict1=json.load(res_text,encoding="utf-8")#文本转化成字典
print(res_text['name'])#方便获取其中的参数值
