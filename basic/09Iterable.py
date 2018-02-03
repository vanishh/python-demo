# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 09:54:39 2018

@author: geyang

讲解迭代Iteration、可迭代对象Iterable、迭代器Iterator
"""
# 迭代Iteration
# 在python中，迭代是通过for ... in完成的
# 
dict1 = {"a":"geyang", "b": 10}
# 迭代key
for key in dict1:
    print(key)
    
# 迭代value
for value in dict1.values():
    print(value)

# 同时迭代key、value
for key, value in dict1.items():
    print(key,value)

# 可以直接作用于for循环的数据类型：
# 1.集合类型，如list、tuple、dict、set、str
# 2.generator: 包括生成器、generator function
# 凡是可以作用于for循环 的对象称为可迭代对象：Iterable

from collections import Iterable
from collections import Iterator

print("list:",isinstance([], Iterable))
print("tuple:",isinstance((), Iterable))
print("dict:",isinstance({}, Iterable))
print("str:",isinstance("abc", Iterable))
print("int:",isinstance(1, Iterable))

# 凡是可以作用于next() 函数的，并不断返回下一个值得对象称为迭代器Iterator
# Iterator对象 表示一个数据流，可以把这个数据流看做是有序序列，提前不需要知道序列的长度，
# Iterator 表示一个惰性计算的序列
# 通过next() 调用不断返回下一个数据，直到没有数据时抛出StopIteration错误
# 生成器即是可迭代对象，也是迭代器
generator1 = (x for x in range(10))
print("generator:", isinstance(generator1, Iterator))

print("list:",isinstance([], Iterator))
print("tuple:",isinstance((), Iterator))
print("dict:",isinstance({}, Iterator))
print("str:",isinstance("abc", Iterator))
print("int:",isinstance(1, Iterator))

# Iterable 和 Iterator的转换

iteratorList = iter([1])
print(isinstance(iteratorList, Iterator))