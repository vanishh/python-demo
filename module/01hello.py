# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:55:07 2018

@author: geyang
"""
# 在python中，每一个.py文件就为一个模块
# 使用模块可以避免与其他模块函数名和变量名冲突
# 不与内置函数名冲突
# 本文件叫01hello的模块（
# 模块命名：模块名要遵循python的命名规范、不要与系统模块名冲突

# 包
# 选择顶层包存放模块，每个包目录下一定会有__init__.py文件（可以是空文件，也可以有代码）
# __init__.py本身也是一个模块，模块名为包名


# __xx__这种变量是特殊变量，有特殊用途，可以被直接引用
__author__ = "Gavin Ge"

# _xx这样的函数或者变量是private权限，不应该直接引用
# 但是python还是可以访问，但从面向对象原理，不直接引用private变量或函数
_userName = ""
_age = 15

import sys

# 正常的函数名，或者变量名是public权限
def test():
    args = sys.argv
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print("hello, %s" % args[1])
    else:
        print("too many argumengts!")

# 定义private函数hello
def _hello(name):
    return "hello, %s" % name

def _hi(name):
    return "hi, %s" % name

def greeting(name):
    if(len(name) > 3):
        return _hello(name)
    else:
        return _hi(name)
    
if __name__ == '__main__':
    test()
    greetResult = greeting("geyang")
