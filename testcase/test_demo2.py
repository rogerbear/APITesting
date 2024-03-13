# -*- coding: utf-8 -*- 
# @Time : 2024/3/12 11:13 
# @Author : roger 
# @File : test_demo2.py

import pytest
from api.test_api import APITestFramework
from common.get_log import GetLog
import run
import allure

# 获取日志器
log = GetLog.get_log()

@pytest.mark.skip("测试数据，不执行")
def test_get_user(api_framework):
    response = api_framework.send_request("GET", "/users/1")
    log.info("状态码为: {}".format(response.status_code))
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["id"] == 1
    assert user_data["username"] == "Bret"

@pytest.fixture
def api_framework():
    return APITestFramework(base_url=run.BASE_URL)
