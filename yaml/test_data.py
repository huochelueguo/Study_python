# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_data.py
@Time:NAME.py@Time:2020/7/30 上午8:45
"""
import yaml
import pytest
import requests

with open('test_data1', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
    # 获取ids,直接输出存在乱码的情况
    list_desc = []
    for desc in data:
        list_desc.append(desc['desc'])


# @pytest.mark.parametrize('datas', data, ids=list_desc)
# class Test_login(object):
#
#     def test_login(self, datas):
#         print(datas['url'])
#         print(datas['body'])
#         r = requests.post(url=datas['url'], data=datas['body'])
#         # print(r.json())
#         test = r.text
#         assert 'success' in test
#
#
# if __name__ == '__main__':
#     pytest.main()
