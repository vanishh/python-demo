# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:53:46 2018

@author: Administrator
"""

# 生成器 generator
# 不必创建完整的list，列表的元素可以通过某种算法推算出来
# 这种一边循环，一边计算的机制，称为生成器generator
generator1 = (x * x for x in range(10))
# <generator object <genexpr> at 0x08EAC960>

# 打印生成器中的元素
for n in generator1:
    print(n)

# 定义generator的另一种方法
# 如果函数定义中包含yield，这个函数就不再是普通函数，而是一个generator
# odd() 不是普通函数，而是generator
def odd():
    print("step 1")
    yield(1) # 遇到yield 中断，返回
    print("step 2")
    yield(3)
    print("step 3")
    yield(5)
    return "DONE"
o = odd()
# generator 每次在调用next() 时执行，遇到yield语句返回，
# 再次执行时，从上次返回的yield出继续执行
#next(o)

for yieldn in o:
    print(yieldn)

# 用for循环调用generator时，拿不到generator的return语句返回值
# 想要拿到return返回值，必须捕获StopIteration 错误
while True:
    try:
        yieldResult = next(o)
        print(yieldResult)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break

# 练习输出fib数列
def fib(num):
    n = 0
    list1 = []
    while n < num:
        if n == 0:
            list1.append(0)
            n += 1
        elif n == 1:
            list1.append(1)
            n += 1
        else:
            nextNum = int(list1[n-1]) + int(list1[n-2])
            list1.append(nextNum)
            n += 1
    return list1

result = fib(5)
print(result)

# IndentationError: unindent does not match any outer indentation level
# 混用TAB 和 空格问题

