# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 23:15:32 2018

@author: geynag
"""
# filter() : 过滤元素的高阶函数
# 用法：filter(返回真值的函数，序列)
# 关键在于正确实现一个判断函数
def isOdd(n):
    return n % 2 == 1

def isEven(n):
    return n % 2 == 0

resultList = list(filter(isOdd, list(range(9))))
resultList2 = list(filter(isEven, tuple(range(9))))

# TypeError: not all arguments converted during string formatting
#resultList3 = list(filter(isEven, "12345")) # 只能作用于序列

# sorted() 高阶函数 用于排序 可以传递映射函数
# sorted函数不修改原序列，返回一个新排序序列
sample = [10, 7, 20, 50, 1, -11, -1]
sortedResult = sorted(sample)
sortedResult1 = sorted(sample, reverse = True)

print(sample) # 不修改原序列
print(sortedResult) # 返回一个新序列

# 调用方式2：按照某个函数作用后的结果排序
keySortedResult = sorted(sample, key = abs)
print(keySortedResult)


