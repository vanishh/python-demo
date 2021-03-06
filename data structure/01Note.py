# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 23:50:39 2018

@author: Administrator
"""

# 第一讲
# 解决问题的效率，和数据的组织方式和空间的利用有关
#例3 写程序计算多项式在给定点x的值
#多项式：f(x) = a0 + a1*x + a2*x^2 + ... +an*x^n
# param_list: 多项式系数，x 底数， n 几次幂
def f(param_list, x, n):
    if len(param_list)-1 != n:
        return
    result = param_list[0]
    for index in range(1, n+1):
        result += param_list[index] * (x ** index)
    return result
list1 = [1, 2]
print(f(list1, 2, 1))

#fx = a0 + a1x + a2x^2 + a3x^3 = a0 + x(a1 + a2x + a3x^2) = a0 + x(a1 + x(a2 + a3x))
#fx = 1 + 2*1 + 3*1 + 4*1 = 10
def f2(param_list, x, n):
    result = param_list[n]
    for index in range(n-1, 0, -1):
        result = param_list[index] + x * result
    result += param_list[0]
    return result
param_list = [1,2,3,4,5]
print(f2(param_list, 1, 4))

# 最大子序列和
# 给定N个整数的序列{A1,A2,A3...An},求函数
# f(i,j)=max{0, 求和Ak(i,j)}的最大值
# 从Ai到Aj连续的一段子列的和
# 方法1：穷举法O(n**3)
def maxSubseqSum1(list1, n):
    maxSum = 0
    for i in range(n):      # i 是子列的左端位置
        for j in range(i,n):  # j 是子列的右端位置
            thisSum = 0     # A[i]到A[j]的子列和
            for k in range(i,j+1):
                thisSum += list1[k]
                if thisSum > maxSum:
                    maxSum = thisSum
    return maxSum

# 方法2：O(n**2)
def maxSubseqSum2(list1, n):
    maxSum = 0
    for i in range(n):
        thisSum = 0
        for j in range(i,n):
            thisSum += list1[j]
            if thisSum > maxSum:
                maxSum = thisSum
    return maxSum

# 方法三：分而治之
# 把大问题拆成小块，然后再合并结果