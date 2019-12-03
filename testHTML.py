# coding=utf-8
import unittest
import testcase1
from testcase1 import Math

'''unittest创建测试报告：用例-集合用例-执行用例-出具测试报告'''
'''创建测试用例'''
#测试类-测试用例
class testunitHtml(unittest.TestCase):
    #数据准备
    def setUp(self):
        self.a=4
        self.b=7
        print("start")
    def test_add(self):#统一使用test开头
        result=Math().add(self.a,self.b)
        print"加法"
        print result

    def test_sub(self):
        result2=Math().sub(self.a,self.b)
        print"减法"
        print result2

    def tearDown(self):
        print("end")

if __name__=="__main__":
    unittest.main()
