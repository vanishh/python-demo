# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:22:23 2018

@author: Administrator
"""

# 匿名函数
# 不需要显示的定义函数，直接传入匿名函数

def f(x):
    return x * x

# 匿名函数的语法为
# lambda 表示匿名函数 冒号前面的x表示函数参数
# 匿名函数的限制 函数体只有一句语句 不用写return
# 匿名函数的优点：函数没有名字 匿名函数也是一个函数对象
func1 = lambda paramName: paramName * paramName 

# 匿名函数也是一个函数对象
# 可以把匿名函数赋值给变量
result = func1(5) 

resultLambda = list(map(lambda x: x * x, range(5)))

# 匿名函数作为返回值
def build(x, y):
    return lambda: x * x + y * y

