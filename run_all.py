#  coding=utf-8
import testHTML
from test_user_login import  *
from lib.emil_test2 import *
from config.config import *
logging.info("==========测试开始============")
'''创建加载器和执行用例'''
'''用例--用例收集容器（TestSuite）--用例加载器(TestLoader/addTest)--用例执行器(TextTestRunner)-执行用例加载器中的用例(runner.run(suite))'''
#创建用例收集容器
suite=unittest.TestSuite()

#创建用例加载器
ts=unittest.TestLoader()
#传入模块名
suite.addTest(ts.loadTestsFromModule(testHTML))
#uite.addTest(ts.loadTestsFromModule(test7))


'''执行用例：
生成用例执行器-生成测试报告 '''

with open(report_file,"wb+") as f:#从配置文件中读取
    runner=unittest.TextTestRunner(stream=f,descriptions="测试报告",verbosity=2)#用例执行器
    runner.run(suite)#传参，集合suite

#verbosity=2，只有1和2的值，2展示的信息更全面一点，如果代码出错，也有错误信息

#发送邮件
send_email(report_file) #从配置文件中读取
logging.info("=========测试结束==========")