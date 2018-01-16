# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 23:54:40 2018

@author: Administrator
"""

# 可以使用types模块中定义的常量来判断类型
import types
# 获取对象信息
# type()函数获取对象类型
print(type(123))
print(type("test"))
print(type(None))

# type函数获取函数或者类信息
print(type(abs))

def compare(number1, number2):
    if type(number1) == type(number2):
        print("%s type is equal to %s" % (number1, number2))
    else:
        print("not equal")
        
compare(100, "test")

print("builein function type:", type(abs) == types.BuiltinFunctionType)
print("function type: ", type(compare) == types.FunctionType)

# isinstance()可以用于判断类型和判断继承关系 优先使用
print("is instance:", isinstance('a', str))
print("is instance:", isinstance([1, 2, 3], list))

# dir()获取一个对象的所有属性和方法
dirResult = dir("ABS")


class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
    
# 获取的属性和方法可以配合getattr()、setattr()、hasattr()方法一起使用
obj = MyObject()
print("has attr x:", hasattr(obj, 'x'))
print(getattr(obj, 'x'))
print("has attr x:", hasattr(obj, 'y'))
print("has attr power:", hasattr(obj, 'power'))
