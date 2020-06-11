import os
import unittest
import time
import HTMLTestRunner_PY3
import app
from script_定义测试用例.test_登录的测试用例 import TpshopTest
# 2 创建测试套件
suite = unittest.TestSuite()
# 3 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TpshopTest))

# 4 定义生成测试报告在哪个目录和报告名称
report_path = app.BASE_DIR + "/report_存放测试报告/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
# 5 使用HTMLTestRunner_PY3生成测试报告
with open(report_path, mode='wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="tpshop注册与登录接口测试报告",
                                               description="作业之测试tpshop的注册和登录")
    # 使用实例化的runner运行测试套件，生成测试报告
    runner.run(suite)
