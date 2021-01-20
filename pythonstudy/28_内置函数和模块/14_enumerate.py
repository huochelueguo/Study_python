# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:14_enumerate.py
@Time:NAME.py@Time:2021/1/20 18:42
"""
"""
作用：返回数组下标
写法：enumerate(可迭代数据, start=)
    start代表从X开始，默认为0
返回值：返回一个枚举，数据+下标组成的元组
"""
l1 = [1, 2, 3, 4, 5]
for i in enumerate(l1):
    print(i)

# 如果仅输出下标
for k, v in enumerate(l1, start=1):
    print(k)