# encoding=utf-8
import unittest
import requests

'''unittest 测试框架'''

#类必须Test开头，继承TestCase才能识别用例类
class TestUserLogin(unittest.TestCase):
    url='http://115.28.108.130:5000/api/user/login/'

    def test_user_login_normal(self):#一条测试用例，必须test_开头
        data={"name":"张三","password":"123456"}
        res=requests.post(url=self.url,data=data)
        #print(res.text)
        self.assertIn(u'成功',res.text)# 断言 是一种方法判断测试是否通过

    def test_user_login_password_wrong(self):
        data={"name":"张三","password":"12456"}
        res=requests.post(url=self.url,data=data)
        self.assertIn(u'失败',res.text)#断言

if __name__=='__main__':
    unittest.main(verbosity=2) #运行本测试类所有
