# -*- coding: utf-8 -*- 
# @Time : 2024/3/12 15:33 
# @Author : roger 
# @File : test_shujian.py

import pytest
from api.test_api import SJTestFramework
from common.get_log import GetLog
import run

# 获取日志器
log = GetLog.get_log()


def test_shujian(api_framework):
    response = api_framework.send_request("GET", "/oauth-center/web/user/info")
    log.info("状态码为: {}".format(response.status_code))
    log.info(response)
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["code"] == "0"
    assert user_data["data"]["email"] == "rogerzhao@digitalgd.com.cn"

@pytest.fixture
def api_framework():
    return SJTestFramework(base_url=run.BASE_URL_SHUJIAN)