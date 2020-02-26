# -*- coding:utf-8 -*-
import os

import pytest

from initilization.driver import Driver
import logging

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
logfile = '../log/logger.txt'
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.NOTSET)  # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

if __name__ == '__main__':
    logging.info("Start to execute automation cases")
    logging.debug("debug test")
    pytest.main(['-sq', '--alluredir', '../result/', 'testcase/books/test_books.py'])
    logging.info("End to execute automation cases")
    os.system('allure generate ../result/ -o ../report/ --clean')
    #os.system('allure open -h 127.0.0.1 -p 8083 ../report/')
