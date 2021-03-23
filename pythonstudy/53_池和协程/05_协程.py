# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:05_协程.py
@Time:2021/3/22 上午9:04
"""
"""
三者的区别:
    进程：资源单位
    线程：执行单位
    协程：这个概念完全由程序员自己想象而来，根本不存在
        作用：单线程下实现并发
        方法：程序员在代码层面进行检测，如果有IO操作，在代码级别进行切换，给CPU感觉像是程序一直在运行，没有IO，提升了效率

多道技术：
    切换+保存状态
    CPU切换的情况：
        1.程序遇到io
        2.程序长时间占用
"""