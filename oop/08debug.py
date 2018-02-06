# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:36:25 2018

@author: Administrator
"""
# 调试程序方式：
# 1.在程序中使用print()打印中间变量值
# 2.使用assert 断言 
# 启动解释器时，可以使用-0参数关闭assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' # 如果assert为true则继续执行，为false则抛出AssertionError
    return 10 / n

def main():
    foo('0')
    
main()

# logging记录

import logging
logging.basicConfig(level=logging.INFO)

def main1():
    n = 0
    logging.info("n = %d" % n)
    print(10 / n)
    
main1()
