# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:42:28 2018

@author: Administrator
"""

# 函数式编程
# 计算指数学意义上的计算，越是抽象的计算，离计算机硬件越远
# 越低级的语言越贴近计算机，抽象程度越低，执行效率高；越高级语言，越贴近计算，抽象程序高

# 函数式编程 是一种抽象程度很高的编程范式
# 纯粹的函数式编程编写的函数没有变量，输入确定，即输出确定；
# 使用变量的程序语言，变量状态不确定，输入产生的输出不确定

# 函数式编程：允许把函数本身作为参数传入另一个函数，还允许返回函数

# python 支持函数式编程，支持使用变量，所以，Python 不是纯函数式编程语言

# 变量可以指向函数
f = abs 
print(f)

print(f(-10)) # 可以通过变量来调用函数

# 函数名也是变量 ，函数名就是指向函数的变量
#abs = 10 
#abs(-10) # TypeError: 'int' object is not callable

# 函数 传入函数参数
# 高阶函数 ：一个函数可以接收函数作为参数
def add_new(x, y, f):
    return f(x) + f(y)

result = add_new(5, -6, abs)
print(result)

# 高阶函数可以把函数作为结果值返回
# 我们在函数中又定义了函数sum，内部函数可以引用外部函数的参数和局部变量
def calc_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

funcResult = calc_sum(1, 2, 3, 4)
funcResult2 = calc_sum(1, 2, 3, 4)

print(funcResult == funcResult2) # 每次返回一个新函数

# 闭包的概念？？
