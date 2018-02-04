# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 22:26:10 2018

@author: Administrator
"""
# 高阶函数
# map()/reduce()函数
def f(x):
    return x * x

# map(函数名，Iterable对象[, Iterable对象]..) 
# map函数，使函数作用在Iterable对象上，返回Iterator

# 例1
r = map(f, list(range(9)))
print(r)  # <map object at 0x0BD1DAF0>
print(list(r))

# 例2：把list所有的数字转换为字符串
r1 = map(str, list(range(9)))
print(list(r1))

# 例3 divide需要两个参数，所以，map函数，需要两个Iterable对象，作为divide的参数
def divide(x, y):
    return x / y

list1 = [2, 3, 4]
list2 = [1, 1, 1]
result = map(divide, list1, list2)
print(list(result))


# reduce(必须接收两个参数的函数，Iterable对象)：函数的结果继续和序列的下一个元素做函数运算
from functools import reduce
def add(x, y):
    return x + y

result = reduce(add, list(range(1,6)))
print(result)

#
#def double(x):
#    return x ** 2
#result2 = reduce(double, list(range(4)))
#print(result2)
# TypeError: double() takes 1 positional argument but 2 were given

# 例：把[1, 2, 3, 4] 转为1234
def combineDigit(x, y):
    return x * 10 + y

result3 = reduce(combineDigit, list(range(5)))
print(result3)

# 例：str转int
DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

result4 = str2int('1230')

# 练习：把list中的字符串转为首字母大写的lsit
list1 = ["GEYANG", "nihao", "Nihao!"]
def normalize(nameList):
    def captial(name):
        captialName = str(name).capitalize()
        return captialName
    return map(captial, nameList)

normalizeList = list(normalize(list1))

# 练习：编写一个prod()函数，可以接收list并利用reduce求乘积
listProd = [1, 2, 3, 4]
def prod(paramList):
    def mutiply(x, y):
        return x * y
    return reduce(mutiply, paramList)

mutiplyResult = prod(listProd)

