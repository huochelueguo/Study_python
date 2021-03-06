# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:01.常用魔术方法.py
@Time:2021/1/22 上午9:26
"""
"""
以 __XX__ 样式的方法都称为魔术方法
"""
class NewAdd():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        # 未修改过的__str__输出为：<__main__.NewAdd object at 0x107ed0df0>
        # 修改过后为返回语句，注意返回必须为字符串
        return '这是修改过的类描述'

    def __del__(self):
        print('生命周期最后调用的一个方法')

    def __add__(self, b):
        print('可以手动改写目前已经存在的魔术方法')
        return 'a和b求和后的值为:a + b * 10 = {}'.format(self.a + b * 10)


if __name__ == '__main__':
    c = NewAdd(2, 2)
    print(c)
    print(c.__add__(3))




