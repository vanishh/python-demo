# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 00:26:35 2018

@author: Administrator
"""
# 判断素数从普通到高效算法思路
# 枚举法
def is_prime(n):
    for index in range(2,n):
        if n % index == 0:
            return False
    return True

# 枚举法的改进
# 如果一个数可以进行因数分解，那么分解得到的两个数，一定一个<= sqrt(n)，另一个>= sqrt(n)
# 所以我们遍历只需要遍历到sqrt(n)
# 12 = 3 X 4 
import math
def is_prime_2(n):
    end = math.ceil(math.sqrt(n))
    for index in range(2, end+1):
        if n % index == 0:
            return False
    return True

print(is_prime_2(53))
