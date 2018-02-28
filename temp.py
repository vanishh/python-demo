# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 00:26:01 2018

@author: Administrator
"""

def countOff(n, m, out):
    out = []
    for index in range(n):
        out.append(0)
#    print(out)
    location = 0
    # 遍历序号，给元素表序号
    for index in range(1, n+1):
        # 数m个，标一个序号
        number = 1
        while number < m:
            if out[location] == 0:
                number += 1
            location = (location + 1) % n
        out[location] = index
    print(out)
countOff(11, 3, [])

