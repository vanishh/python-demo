# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 如果函数写在文件中 使用 from fimename import fun_name
import math
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

n = my_abs(-10)
print(n)

# 返回多个值 本质是返回一个tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

def power(x, n):
    result = 1
    while n > 0:
        result = result * x
        n = n - 1
    return result

result1 = power(10, 3)

        