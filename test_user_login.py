# coding=utf-8
import unittest
from lib.read_execl import *
from lib.case_log import *
class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  #整个测试类只执行一次
        cls.data_list=execl_to_list(os.path.join(data_path,"test_user_data.xlsx"),"TestUserLogin") #读取该测试类
         # cls.data_list 同 self.data_list 都是类的公共属性

    def test_user_login_normal(self):
        case_data=get_test_data(self.data_list,'test_user_login_normal') #从数据列表中查询
        if not case_data: # 有可能为空
            logging.error("用例数据不存在")

        url=case_data.get('url') #从字典中取数据，execl中的标题也必须是 url
        data=case_data.get('data').encode('utf-8') # 注意字符串格式，需要用json.loads(）转化成字典格式
        expect_res=case_data.get('expect_res').encode('utf-8')#期望数据

        res=requests.post(url=url,data=json.loads(data)) #表单请求，数据转化成字典格式
        res1=res.text.encode('utf-8')
        '''
        logging.info("测试用例：{}".format('test_user_login_normal'))
        logging.info("url:{}".format(url))
        logging.info("请求参数：{}".format(data.encode('utf-8')))
        logging.info("期望结果:{}".format(expect_res.encode('utf-8')))
        logging.info("实际结果：{}".format(res.text.encode('utf-8')))
        '''
        log_case_info('test_user_login_normal', url, data, expect_res, res1)  # 输出log
        self.assertEqual(res1,expect_res) #断言
        print(res.text)

if __name__=='__main__':
    unittest.main(verbosity=2)