# encoding=utf-8
'''用于测试的类和方法'''
import requests

#第一个类
class Math():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b

#第二个类：requests
class HttpRequest:
    def get(self,url,param):
        res=requests.get(url,param)
        return res.json()
    def post(self,url,param):
        res=requests.post(url,param)
        return res.json()

