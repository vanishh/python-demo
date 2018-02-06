# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:01:04 2018

@author: Administrator
"""

# 异常处理
# try except finally
# 如果输入为0，会产生一个ZeroDivisionError异常
def func():
    try:
        print("try...")
        number = int(input())
        r = 10 / number
        print("result:", r)
    except ZeroDivisionError as e:
        print("except:", e)
    else:
        print("no error!") 
        # 可以在except后添加else语句，如果没有异常则执行else块
    finally:
        print("finally...")
    print("END")
    
func()

# 程序的错误也是class，所有的错误都是从BaseException中继承
# 捕获异常顺序:先捕获子类，再捕获父类
# 调用链的异常捕获：可以垮调用捕获异常

# 记录错误
# logging模块
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except BaseException as e:
        logging.exception(e)
main()
print("END")  # 程序出错，捕获后可以正常退出

# 自定义错误类型
# 错误类型是一个Python类，因此可以自定义一个错误类，并在错误发生时抛出
# 在必要的时候才定义自定义错误类型
# 通常使用內建错误类型ValueError、TypeError
class FooError(ValueError):
    pass

def fooRaise(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid vale: %s" % s) # 当遇到错误情况时，抛出错误 raise
    return 10 / n

fooRaise('0')

# reraise
# 如果捕获的异常不知道怎么处理，可以再抛出
def fooReraise(s):
    n = int(s)
    if n == 0:
        raise ValueError("invalid value: %s" % s)
    return 10 / n

def barReraise():
    try:
        fooReraise('0')
    except ValueError as e:
        print("ValueError!!") # 记录一下
        raise
        
barReraise()