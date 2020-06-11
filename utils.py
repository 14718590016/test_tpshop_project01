import json
import logging.handlers

import app


def basic_log_config():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置日志级别
    logger.setLevel(level=logging.INFO)
    # 3.创建每日生成一个日志文件的处理器
    # filename=文件保存路径   when=生成时间  interval=间隔时间   backupCount=最高保存数，超过删除
    lht = logging.handlers.TimedRotatingFileHandler(filename=app.BASE_DIR + "/log_日志/ihrm.log", when="M",
                                                    interval=1,
                                                    backupCount=3, encoding='utf-8')
    # 4.创建控制台的处理器
    ls = logging.StreamHandler()
    # 5.创建格式化器
    lf = logging.Formatter(
        fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 6.将格式化器绑定到日志处理器和控制台处理器中
    lht.setFormatter(lf)
    ls.setFormatter(lf)
    # 7.将处理器绑定到日志器
    logger.addHandler(ls)
    logger.addHandler(lht)


# 编写读取注册数据的函数
def read_data(filepath):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 遍历json格式的数据文件，并把数据处理成列表元组形式（[(),(),()]）添加到空列表中
        result_list = list()
        for data in jsonData:
            result_list.append(tuple(data.values()))

    print("抽取的数据为：", result_list)
    return result_list
