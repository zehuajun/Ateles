#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 这个函数用来计算文件哈希值，输入文件地址，输出md5哈希值
def md5(file_name):
    import hashlib

    with open(file_name, "rb") as file:
        data = file.read()
    return hashlib.md5(data).hexdigest()
