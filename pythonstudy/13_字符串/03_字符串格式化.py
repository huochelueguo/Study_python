# 1.字符串格式化使用 %s
str1 = "%s"
print("格式字符串使用: %s " % str1)

# 2.整数格式化使用 %d
int1 = 0
print("整数格式化使用%d ：" % int1)

# 3.Python3.6版本新特性，使用f-string
# f-string是一个文字字符串，前缀为’f’，其中包含大括号内的表达式。表达式会将大括号中的内容替换为其值
str2 = "格式化字符换新方法,使用f开头输出内容，大括号中加上字符串名称即可"
print(f'python3.6新特性:{str2}')

# 4.f-string中还可以带函数或表达式等
print(f'可以直接输出运算内容5+3 = {5+3}')
list1 = [1, 2, 3, 4, 5]
print(f'列表list1长度为 ： {len(list1)}')

# 5.f-string中灵活使用单双引号，保证不和外部定界引号冲突即可
print(f'灵活使用引号，如果要输出双引号，外部可以使用：{"单引号  "}')
print(f'''灵活使用引号，如果输出内容需要有单引号，那外部可以使用：{"3引号 "} ''')
print(f"灵活使用引号，如果输出内容需要单引号，外部也可以使用：{'双引号'}")
