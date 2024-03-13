# -*- coding: utf-8 -*- 
# @Time : 2024/3/12 11:14 
# @Author : roger 
# @File : test_api.py

import requests
from config import config


class APITestFramework:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def send_request(self, method, path, data=None, headers=None):
        url = self.base_url + path
        response = self.session.request(method, url, json=data, headers=headers)
        return response


class SJTestFramework:
    def __init__(self, base_url):
        self.base_url = base_url
        self.request = requests

    def send_request(self, method, path, data=None, headers=None):
        url = self.base_url + path
        response = self.request.request(method, url, json=data, headers=config.headers, cookies=config.cookies)
        return response
