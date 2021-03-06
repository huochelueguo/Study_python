# 切整个对象的几个方法
list1 = [1, 2, 3, 4, 5]
print(list1[:])
print(list1[::])
print(list1[0:])

# 切对象的部分,步长为空，默认为1
list1 = [1, 2, 3, 4, 5]
print(list1[0:3])

# 切对象的部分，有步长,如下输出[1, 3]
list1 = [1, 2, 3, 4, 5, 6]
print(list1[0:4:2])

# 切对象的部分，有步长，其他几个元素为空时，按照从头到尾切
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(f'只有步长的切片，按照步长从头切到尾部{list1[::2]}')


