# -*- coding: utf-8 -*- 
# @Time : 2024/3/11 16:33 
# @Author : roger 
# @File : run.py

import pytest
import os

BASE_URL = "https://jsonplaceholder.typicode.com"
BASE_URL_SHUJIAN = "https://shujian.digitalgd.com.cn"

# 获取脚本的绝对路径
ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)

if __name__ == "__main__":
    pytest.main(["-v", "--html=reports/test_report.html", "testcase"])
