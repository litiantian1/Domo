# coding=utf-8
import unittest
import json
from lib.read_execl import *
import sys

sys.path.append('../..') # 统一将包的搜索路径提升至项目根目录下
from config.config import *
class TestUserReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list=execl_to_list(os.path.join(data_path,"test_user_data.xlsx"),"TestUserReg")

    def test_user_reg_normal(self):
        case_data=get_test_data(self.data_list,"test_user_reg_normal")
        if not case_data:
            print("用例数据不存在")
        url=case_data.get('url')
        data=json.loads(case_data.get('data'))
        expect_res=case_data.get('expect_res')
        name=data.get("name")#范冰冰
        #print url
        #print data

        #发送请求
        res=requests.post(url=url,data=data)#data=data 也可以
        #响应断言（整体断言）
        #str=res.text.encode("utf-8") # unicode转化成字符串
        #print(type(str))
        #dict=json.loads(str)
        #print(dict)
        print res.text
       # self.assertEqual(res.text,expect_res)
        print(res.text)

if __name__=='__main__':
    unittest.main(verbosity=2)
