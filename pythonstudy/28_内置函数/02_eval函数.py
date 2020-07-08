# eval函数作用：
# 1、字符串转换
# 2、返回传入字符串的表达式的结果
# 3、可将看起来像列表的字符串重新转换为列表

a = eval('5 * 10')
print(f'a值为 {a},类型为{type(a)}')
# a值为 50,类型为<class 'int'>

b = eval('10 / 3')
print(f'a值为 {b},类型为{type(b)}')
# a值为 3.3333333333333335,类型为<class 'float'>

c = eval('123')
print(f'a值为 {c},类型为{type(c)}')
# a值为 123,类型为<class 'int'>

str1 = " ['1709020230', '1707030416', '0', '0', '0']  "
d = eval(str1)
print(f'a值为 {d},类型为{type(d)}')
# a值为 ['1709020230', '1707030416', '0', '0', '0'],类型为<class 'list'>
