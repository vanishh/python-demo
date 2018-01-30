# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:51:56 2018

@author: Administrator
"""
# 比较3个数的大小
'''
x = int(input("请输入x:"))
y = int(input("请输入y:"))
z = int(input("请输入z:"))

if x > y:
    if z > x:
        print("%d最大" % (z))
    elif x > z:
        print("%d最大" % (x))
    else:
        print("%d 和%d相同并最大" % (x, z))
elif x < y:
    if y > z:
        print("%d最大" % (y))
    elif z > y:
        print("%d最大" % (z))
    else:
        print("%d和%d最大" % (z, y))  
else:
    if y == z :
        print("%d,%d,%d相同" % (x, y, z))
    elif y > z:
        print("%d和%d最大" % (x, y))
    else:
        print("%d最大" % (z))
'''
# 打印水仙花数
# 题目16：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
#      例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
# 思路：分解出个位、十位、百位
'''
list1 = []
for index in range(100, 1000):
    firstNumber = index // 100
    secondNumber = index % 100 // 10
    lastNumber = index % 100 % 10

    if (firstNumber ** 3 + secondNumber ** 3 + lastNumber ** 3) == index:
        list1.append(index)

print(list1)
'''
# 题目17：打印出如下图案（菱形）
#  
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
'''
for index in range(1, 8, 2):
    print(("*" * index).center(7, ' '))
    if index == 7:
        for indexA in range(5, 0, -2):
            print(("*" * indexA).center(7, ' '))
'''
# 题目18：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。(用列表推导式)
'''
list2 = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                data = i * 100 + j * 10 + k
                list2.append(data)

print(list2)
'''
# 题目19：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
# 增加条件：相邻位不相同
list3 = []
for index in range(10000, 100000):
    one = index % 10
    two = index % 100 // 10
    three = index % 1000 // 100
    four = index // 1000 % 10  # 或者 index % 10000 // 1000
    five = index // 10000
    if one == five and two == four and one != two and two != three:
        list3.append(index)

print(list3)