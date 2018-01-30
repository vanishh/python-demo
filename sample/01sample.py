# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 例1：计算m ~ n之间整数的和
def sum(m, n):
    sumAll = 0
    if m > n:
        return
    else:
        while(m <= n):
            sumAll += m
            m += 1
        return sumAll
    
result = sum(4, 2)
result1 = sum(-5, 8)

# 例2：计算两数较大的数
def max(numA, numB):
    if int(numA) > int(numB):
        return int(numA)
    else:
        return int(numB)
    
resultMax = max(-5, 8)
resultMax1 = max(12.3, 13.3)

# 例3：打印数字金字塔
def pyramid(rows):
    currentRow = 1
    space = rows - 1
    if rows > 9 and rows < 0:
        return
    else:
        while currentRow <= rows:
            print(' ' * space + (str(currentRow) + ' ') * currentRow)
            space -= 1
            currentRow += 1

pyramid(-1)

# 例4： 实现符号函数
# 若 x > 0, sign(x) = 1; 若x = 0, sign(x) = 0; x < 0 sign(x) = -1
def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1
    
resultSign = sign(9)
resultSign1 = sign(0)
resultSign2 = sign(-8)

# 例5：求奇数和
# 实现一个判断奇偶性的函数，再计算整数中所有奇数的和
# even(n)
def even(numA):
    if (numA % 2) == 0:
        return True

