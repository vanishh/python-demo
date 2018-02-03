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

# 习题5-2：使用函数求奇数和
# 实现一个判断奇偶性的函数，再计算N个整数中所有奇数的和
# https://pintia.cn/problem-sets/12/problems/302

# 其中函数even将根据用户传入的参数n的奇偶性返回相应值：当n为偶数时返回1，否则返回0。
def even(numA):
    if (numA % 2) == 0:
        return 1
    else:
        return 0
    
# 函数OddSum负责计算并返回传入的N个整数List[]中所有奇数的和。
def oddSum(list1, n):
    result = 0
    for index in list1:
        if even(index) == 0:  # 如果是奇数，累加
            result += index
    return result

list1 = [2, -3, 7, 88, 0, 15]
result = oddSum(list1, len(list1))
print(result)

# 习题5-3 使用函数计算两点间的距离
# 本题要求实现一个函数，对给定平面任意两点坐标(x1, y1) (x2, y2)，求两点的距离
# 用户传入的参数为平面上两点的坐标，函数dist返回两点之间的距离

import math
def dist(x1, y1, x2, y2):
    distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return round(math.sqrt(distance), 2)

dist = dist(10, 10, 200, 100)
print(dist)
    
# 小结：
# round(a, 保留位数):四舍五入
# import math 导入math模块，使用math.sqrt() 、math.ceil():向上取整 math.floor()：向下取整

# 习题5-4 使用函数求素数和
# 本题要求实现一个判断素数的简单函数、以及利用该函数计算给定区间内素数和的函数。
# 素数就是只能被1和自身整除的正整数。注意：1不是素数，2是素数。
# prime() 判断参数是否是素数，是返回1，否则返回0
def prime(number):
    for index in range(2, number):
        if number % index == 0:
            return 0
    return 1

#result = prime(4)
# 函数PrimeSum返回区间[m, n]内所有素数的和。题目保证用户传入的参数m≤n。
def primeSum(m, n):
    sumResult = 0
    if m > n:
        return 
    else:
        for index in range(m, n+1):
            if prime(index):
                sumResult += index
    return sumResult
result = primeSum(-1, 10)

# 习题5-5 使用函数统计指定数字的个数 
# 本题要求实现一个统计整数中指定数字的个数的简单函数。
# countDight(number, digit) 
#其中number是不超过长整型的整数，digit为[0, 9]区间内的整数。函数CountDigit应返回number中digit出现的次数。
def countDigit(number, digit):
    count = 0
    if digit < 0 and digit > 9:
        return
    if not str(number).isdigit():
        return
    strNumber = str(number)
    print(strNumber)
    for e in strNumber:
        if e == str(digit):
            count += 1
    return count

result = countDigit(100444, 4)
print(result)

#习题5-6 使用函数输出水仙花数
# 水仙花数是指一个N位正整数（N≥3），它的每个位上的数字的N次幂之和等于它本身.
#​​ 本题要求编写两个函数，一个判断给定整数是否水仙花数，
# 另一个按从小到大的顺序打印出给定区间(m,n)内所有的水仙花数。
def narcissistic(number):
    length = len(str(number))
    if length < 3:
        return
    data = 0
    for index in range(0,length):
        data += int(str(number)[index]) ** length
        
    # 判断是否是水仙花数
    if data == number:
        return 1  
    else:
        return 0

#print(narcissistic(153))
        
#函数PrintN则打印开区间(m, n)内所有的水仙花数，每个数字占一行。题目保证100≤m≤n≤10000。
def printN(m, n):
    if m > n:
        return
    if not (m >= 100 and n <= 10000):
        return
    for index in range(m, n):
        if narcissistic(index) == 1:
            print('%d\n' % index)
printN(153, 400)

#习题5-7 使用函数求余弦函数的近似值
#本题要求实现一个函数，用下列公式求cos(x)的近似值，精确到最后一项的绝对值小于e：
#cos(x)=x​0/0! − x​2/2! + x​4​/4! − x​6/6! + ⋯

#其中用户传入的参数为误差上限e和自变量x；
#函数funcos应返回用给定公式计算出来、并且满足误差要求的cos(x)的近似值。输入输出均在双精度范围内。
# 0! = 1 1! = 1
# 1 ** 0 = 1
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def funcos(e, x):
    result = 0
    tempExpress = 0
    power = 0
    symbol = -1
    symbolPower = 0
    while True:
        symbolTemp = symbol ** symbolPower
        tempExpress = (x ** power) / factorial(power)
        if tempExpress <= e:
            return '%.6f' % result
        else:
            result += symbolTemp * tempExpress
            symbolPower += 1
            power += 2
        
print(funcos(0.01, 0))