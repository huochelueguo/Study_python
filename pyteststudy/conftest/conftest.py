# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:conftest2.py
@Time:NAME.py@Time:2020/7/11 15:31
"""
import pytest


@pytest.fixture(params=['数据组1', '数据组2'])
def login_data(request):
    print(f'本次测试使用的数据是{request.param}')
    yield 2
    print(f'测试执行完输出')


@pytest.fixture(scope='class')
def login_data2():
    a = 5
    b = 5
    return a, b


@pytest.fixture()
def login_data3():
    print(f'执行测试用例的前期')
    yield 5
    print('测试用例执行完成后')



