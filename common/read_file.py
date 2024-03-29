# -*- coding: utf-8 -*- 
# @Time : 2024/3/12 09:54 
# @Author : roger 
# @File : read_file.py

import run
import json


def read_txt(filename):
    filepath = run.BASE_DIR + "/data/" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()


# 规定test_data.json格式固定, 一级key值固定为api文件同名, attr为key值
def read_json(attr):
    # 1、新建空列表，接收解析结果
    arr = list()
    # 2、解析文件组织数据添加进列表
    with open(run.BASE_DIR + "/data/test_data.json", "r", encoding="utf-8") as f:
        result = json.load(f)
        for i in result[attr]:
            row = i.values()
            arr.append(list(row))
        return arr