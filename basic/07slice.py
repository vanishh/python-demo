# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 高级特性
# 切片操作符 用于取元素

# 列表
list1 = [1, 2, 3, 4, 5]
print(list1[0:3]) # 取从索引0 到索引3，不包括3
print(list1[:3]) # 如果第一个索引为0，还可以省略

list2 = list(range(100))
#print(list2)
# 取后10个
print(list2[-10:])
# 取前10个 每两个取一个
print(list2[:10:2])

# 取从头到尾 每5个取一个
print(list2[::5])

# 元组
tuple1 = (1, 2, 3, 4)
print(tuple1[:3])  # 元组切片为元组

# 字符串
string1 = "test"
print(string1[0:1])

# 练习 使用切片 实现去除字符串的前后空格
def trim(s):
    
    return s
    

