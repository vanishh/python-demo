# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 演示使用list
# 初始化list
classmates = ['geyang', 'nihao']
# 在list末尾添加一个元素
classmates.append("last")
# 在list末尾删除一个元素, 或者指定位置元素pop(index)

# insert插入一个元素， insert(index, element)
classmates.insert(1, "one")

# 删除元素
# 删除末尾的元素
classmate2 = ["zero", "one", "two"]
element = classmate2.pop()

# 用del 函数删除元素
del(classmate2[0])

# remove(元素值)
classmate2.remove("geyang") #ValueError: list.remove(x): x not in list


# 常用list 方法
list1 = list(range(9))

# 返回值为NoneType （这是没有返回值？？） 
# 改变原有list
result = list1.reverse()

list1.sort()

list2 = list1.copy() 

# 演示使用tuple
tuple1 = ("geyang", "nihao", ["zero", "one"])

# 访问元组
print(tuple1[0])

# 修改元组
# 元组中的元素值是不允许被修改和删除的
#tuple1[0] = "nihao" #TypeError: 'tuple' object does not support item assignment
tuple1[2][0] = "change"
del tuple1 # 可以用del 语句删除元组变量

tuple3 = tuple(range(5))

# 截取元组 切片
print("截取元素0:3", tuple3[0:3])

# 多维元组
tuple4 = ("geyang", (1, 2, 3), True, 15)
print(tuple4[1][:])

# 元组函数
# len()、max()、min()为通用函数
tupleTemp = tuple("geyang") # tuple()可以转换字符串为字符元组，转换list