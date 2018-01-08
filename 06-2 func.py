# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 递归函数：fact(n) = fact(n -1) * n
# 理论上 所有的递归函数都可以写成循环方式
# 使用递归函数，需要防止栈溢出
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(10))

# 如果递归调用的层数过深，会造成栈溢出
# 解决递归调用栈溢出的方法是 尾递归优化
# 尾递归指，函数在返回的时候，调用自身，并且return语句不能包含表达式

# 编译器或者解释器会对尾递归做优化，使递归本身无论调用多少次
# 都只占一个帧 不出现栈溢出的情况

def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

#fact2(100000000000000)  # 经测试 还是会出现栈溢出现象
# python 标准的解释器 没有针对尾递归做优化 还是会出现栈溢出问题