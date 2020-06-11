import logging

import requests, unittest, pymysql

import app
from api_封装接口.zuoye_注册 import Register
from api_封装接口.zuoye_登录 import Sign_in
from utils import read_data
from parameterized import parameterized


class TpshopTest(unittest.TestCase):
    def setUp(self):
        # 实例化session
        self.session = requests.Session()
        # 初始化登录
        self.login_api = Sign_in()
        # 初始化注册API
        self.regist_api = Register()
        # 初始化数据库连接        
        self.conn = pymysql.connect(host='localhost', user='root', password='root', database='tpshop2.0', charset='utf8')
        # 获取游标        
        self.cursor = self.conn.cursor()


    def tearDown(self):
        self.session.close()
        self.cursor.close()
        self.conn.close()



    # 定义json文件路径并当做参数传入
    filepath = app.BASE_DIR + "/data_测试数据/register_data.json"

    @parameterized.expand(read_data(filepath))
    def test01_reg_and_login(self, username, register_word, login_password, status, reg_msg, login_msg, http_code):
        # 调用注册的获取验证码接口
        self.regist_api.get_verify(self.session)
        # 调用注册接口
        data = {"auth_code": "TPSHOP", "scene": "1", "username": username,
                "verify_code": "8888", "password": register_word, "password2": register_word}
        response_reg = self.regist_api.regist(self.session, data)
        jsonData = response_reg.json()

        # 断言注册结果
        self.assertEqual(status, response_reg.json().get('status'))
        self.assertEqual(reg_msg, response_reg.json().get('msg'))
        self.assertEqual(http_code, response_reg.status_code)
        # 打印日志信息
        logging.info(jsonData)

        # 在数据库中查询注册结果(查询数据库的会员表中mobile是否有新注册的号码，
        # 通过注册返回的信息"result":{"mobile":"xxxxxx"},用.get提取到)
        self.cursor.execute("select mobile from tp_users where mobile= {}".format(
            jsonData.get('result').get('mobile')))
        # 获取表格中指针下的第一个数据(由于查询的表格只查询了指定值，所以只有一个数据)
        result = self.cursor.fetchone()[0]
        # 断言数据库中的查询结果        
        self.assertEqual(username, result)


        # 调用登录的获取验证码的接口
        self.login_api.get_verify(self.session)
        # 调用登录接口
        data = {
            "username": username,
            "password": login_password,
            "verify_code": "8888"
        }
        response_login = self.login_api.login(self.session, data=data)
        logging.info(response_login.json())

        # 断言登录结果
        self.assertEqual(status, response_login.json().get('status'))
        self.assertEqual(login_msg, response_login.json().get('msg'))
        self.assertEqual(http_code, response_login.status_code)
