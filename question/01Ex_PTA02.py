# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:43:32 2018

@author: Administrator
"""
#习题6-1 分类统计字符个数（15 分）
#本题要求实现一个函数，统计给定字符串中英文字母、空格或回车、数字字符和其他字符的个数。
def stringCount(inputStr):
    blankCount = 0
    alphaCount = 0
    digitCount = 0
    otherCount = 0
    inputStr = str(inputStr)
    for char in inputStr:
        if str(char) == ' ' or str(char) == '\n':
            blankCount += 1
        elif str(char).isalpha():
            alphaCount += 1
        elif str(char).isdigit():
            digitCount += 1
        else:
            otherCount += 1
    print("letter = %d, blank = %d, digit = %d, other = %d" % (alphaCount, blankCount, digitCount, otherCount))

inputStr = input()
stringCount(inputStr)

# 习题6-2 使用函数求特殊a串数列和（20 分）
# 给定两个均不超过9的正整数a和n，要求编写函数求a+aa+aaa++⋯+aa⋯a（n个a）之和。
# 其中函数fn须返回的是n个a组成的数字
def fn(a, n):
    result = ''
    if (a > 9 or a < 0) or (n > 9 or n < 0):
        return
    else:
        for index in range(1, n+1):
            # n = 3  aaa
            result += str(a)
        return int(result)
#print(fn(3, 3))
        
# sumA返回要求的和。
def sumA(a, n):
    sumResult = 0
    message = ''
    for index in range(1, n+1):
        sumResult += fn(a, index)
        message += str(fn(a, index)) + '+'
    print(message)
    return sumResult

result = sumA(2, 3)

# 习题6-3 使用函数输出指定范围内的完数（20 分）
# 本题要求实现一个计算整数因子和的简单函数，并利用其实现另一个函数，
# 输出两正整数m和n（0<m≤n≤10000）之间的所有完数。所谓完数就是该数恰好等于除自身外的因子之和。例如：6=1+2+3，其中1、2、3为6的因子。
# 函数factorsum须返回int number的因子和；
def factorSum(number):
    sumResult = 0
    if number == 1:
        return 1
    for index in range(1, number):
        if number % index == 0:
            sumResult += index
    return sumResult
#print(factorSum(4))
#print(factorSum(1))

# 函数PrintPN要逐行输出给定范围[m, n]内每个完数的因子累加形式的分解式，
# 每个完数占一行，格式为“完数 = 因子1 + 因子2 + ... + 因子k”，其中完数和因子均按递增顺序给出。如果给定区间内没有完数，则输出一行“No perfect number”。

def printPN(m, n):
    if m <= 0 or m > n or n > 10000:
        return
    else:
        for index in range(m, n+1):
            if index == 1:
                print("1 is a perfect number")
                print("1 = 1")
            elif factorSum(index) == index:
                message = '%d = ' % index
                for j in range(1, index):
                    if index % j == 0:
                        message += '%d + '%j
                print(message[:len(message)-2])
#                    print(message)
                
printPN(1, 30)

# 小知识点：
# 可以使用切片来截取子字符串

# 习题6-4 使用函数输出指定范围内的Fibonacci数（20 分）
# 本题要求实现一个计算Fibonacci数的简单函数，并利用其实现另一个函数，
# 输出两正整数m和n（0<m≤n≤10000）之间的所有Fibonacci数。所谓Fibonacci数列就是满足任一项数字是前两项的和（最开始两项均定义为1）的数列。
# 1 1 2 3 5 8 13

# 函数fib须返回第n项Fibonacci数；n 为项数
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

# 函数PrintFN要在一行中输出给定范围[m, n]内的所有Fibonacci数，
# 相邻数字间有一个空格，行末不得有多余空格。如果给定区间内没有Fibonacci数，则输出一行“No Fibonacci number”。
def printFN(m, n):
    if m <= 0 or m > n or n > 10000:
        return
    else:
        message = ''
        for index in range(1, n):
            if fib(index) > n:
                break
            if fib(index) >= m and fib(index) <= n:
                message += str(fib(index)) + ' '       
        print(message)

print("fib(%d) = %d" % (7, fib(7)))
printFN(20, 100)


#习题6-5 使用函数验证哥德巴赫猜想（20 分）
#本题要求实现一个判断素数的简单函数，并利用该函数验证哥德巴赫猜想：任何一个不小于6的偶数均可表示为两个奇素数之和。
#素数就是只能被1和自身整除的正整数。注意：1不是素数，2是素数。

#函数prime当用户传入参数p为素数时返回1，否则返回0
def prime(p):
    for index in range(2, p):
        if p % index == 0:
            return 0
    return 1

# 函数Goldbach按照格式“n=p+q”输出n的素数分解，其中p≤q均为素数。
# 又因为这样的分解不唯一（例如24可以分解为5+19，还可以分解为7+17），要求必须输出所有解中p最小的解。
def goldBach(n):
    for p in range(2, n):
        # 因为分解为两个素数，首先p需要为素数
        if prime(p):
            # 如果q为素数，终止
            if prime(n - p):
                print("%d=%d+%d"% (n, p, n-p))
                break
                
start = int(input())
end = int(input())
if start < 6:
    m = 6
if start % 2:
    start += 1
for index in range(start , end+1, 2):
    goldBach(index)
    
#习题6-6 使用函数输出一个整数的逆序数（20 分）
#本题要求实现一个求整数的逆序数的简单函数。
#函数reverse须返回用户传入的整型number的逆序数。
def reverse(number):
    strResult = []
    result = ''
    if number < 0:
        strResult.append('-')
        for index in str(abs(number)):
            strResult.insert(1, index)
    else:
        for index in str(number):
            strResult.insert(0, index)
    for char in strResult:
        result += char
    return int(result)

print(reverse(-12340))


#练习8-8 移动字母（10 分）
#本题要求编写函数，将输入字符串的前3个字符移到最后。
def shift(inputStr):
    if len(inputStr) < 3:
        return
    return inputStr[3:] + inputStr[:3]

inputStr = input()
print(shift(inputStr))

#习题8-1 拆分实数的整数与小数部分（15 分）
#本题要求实现一个拆分实数的整数与小数部分的简单函数
import math
def splitFloat(floatNumber):
    intPart = math.floor(floatNumber)
    floatPart = floatNumber - intPart
    return intPart, floatPart

floatNumber = float(input())
intPart, floatPart = splitFloat(floatNumber)
print("The integer part is %d" % intPart)
print("The fractional part is %s" % floatPart)


#习题8-4 报数（20 分）
#报数游戏是这样的：有n个人围成一圈，按顺序从1到n编好号。从第一个人开始报数，报到m（<n）的人退出圈子；下一个人从1开始报数，报到m的人退出圈子。如此下去，直到留下最后一个人。
#
#本题要求编写函数，给出每个人的退出顺序编号。
# n为初始人数，m为游戏规定的退出位次，退出顺序编号存在out中
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

#习题8-6 删除字符（20 分）
#本题要求实现一个删除字符串中的指定字符的简单函数。
def delChar(inputStr, char):
    count = 0
    inputStr = list(inputStr) 
    print(inputStr)
    for index in inputStr:
        if char == index:
            del(inputStr[count]) # del()函数，直接删除元素
            continue
        count += 1
    outputStr = ''
    for index in inputStr:
        outputStr += index
    return outputStr

char = input()
inputStr = input()
print(delChar(inputStr, char))

# 小知识点：
# str 转 list: list(str)
# list 转 str: ''.join(list)
# del(list[index]):删除list指点元素

#习题8-8 判断回文字符串（20 分）
#本题要求编写函数，判断给定的一串字符是否为“回文”。所谓“回文”是指顺读和倒读都一样的字符串。如“XYZYX”和“xyzzyx”都是回文。
# 编写函数，判断输入的字符串是否是回文。是返回true
def palindrmone(inputStr):
    if len(inputStr) == 1 or len(inputStr) == 0 or inputStr == None:
        return True
    else:
        if inputStr[0] == inputStr[len(inputStr)-1]:
            return palindrmone(inputStr[1:-1])
        else:
            return False

print(palindrmone("t"))
print(palindrmone("tt"))
print(palindrmone("tst"))
print(palindrmone("test"))

# 方法2：
def palindrmone2(inputStr):
    for index in range(len(inputStr) // 2):
        if inputStr[index] != inputStr[-(index + 1)]:
            return False
    return True

print(palindrmone2("tt"))
print(palindrmone2("tet"))
print(palindrmone2("teet"))
print(palindrmone2("teet3"))
            
# 小知识点：
# 索引
print("test"[-1]) # -1 表示最后一个
# 切片
print("test"[:])   # 表示从头到尾
print("test"[0:])  # 表示从0开始，到尾
print("test"[1:3]) # [1, 3]表示[1, 3) 左闭右开
print("test"[:-1]) # -1 表示倒数第一个，[0，倒数第一个)
print("test"[:-2]) # -2 表示倒数第2个
print("test"[1:-1]) # 去第一个和最后一个
#print("te"[1:-1])

list(range(1,4)) # range(1,4) [1,4)  左闭右开

for index in range(0):
    print(index) # 什么也没有打印
    

#习题9-2 计算两个复数之积（15 分）
#本题要求实现一个计算复数之积的简单函数。
class Complex(object):
    # 定义复数的属性
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        print("%d+(%d)i" % (self.real, self.imag))
        
    def add(self, anotherComplex):
        self.real += anotherComplex.real
        self.imag += anotherComplex.imag
    
    def minus(self, anotherComplex):
        self.real -= anotherComplex.real
        self.imag -= anotherComplex.imag

    def mutiply(self, anotherComplex):
        realReuslt = (self.real * anotherComplex.real) - (self.imag * anotherComplex.imag)
        imagResult = (self.imag * anotherComplex.real) + (self.real * anotherComplex.imag)
        self.real = realReuslt
        self.imag = imagResult

    def toString(self):
        print("%d+(%d)i" % (self.real, self.imag))
        
complex1 = Complex(3,4)
complex2 = Complex(5,6)
#complex1.add(complex2)
complex1.mutiply(complex2) # 程序有bug，复数乘积出错
print(complex1.toString())

#习题9-6 按等级统计学生成绩（20 分）
#本题要求实现一个根据学生成绩设置其等级，并统计不及格人数的简单函数。
#set_grade函数需要根据学生的成绩score设置其等级grade。
#等级设置：85－100为A，70－84为B，60－69为C，0－59为D。同时，set_grade还需要返回不及格的人数。
class Student(object):
    
    def __init__(self, num, name, score, grade):
        self.num = num
        self.name = name
        self.score = score
        self.grade = grade
        
    def set_grade(self):
        if self.score <= 100 and self.score >= 85:
            self.grade = "A"
        elif self.score >= 70:
            self.grade = "B"
        elif self.score >= 60:
            self.grade = "C"
        else:
            self.grade = "D"
        
    def get_grade(self):
        return self.grade
    
student1 = Student("300031", "geyang", 80, "N")
student1.set_grade()
print(student1.get_grade())

#练习10-1 使用递归函数计算1到n之和（10 分）
#本题要求实现一个用递归计算1+2+3+…+n的和的简单函数。
# 非递归
def sum(n):
    if n <= 0:
        return 0
    sumResult = 0
    for index in range(1,n + 1):
        sumResult += index
    return sumResult

print(sum(10))

# 递归
def sumRecur(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return n + sumRecur(n - 1)

print(sumRecur(10))

#习题10-1 判断满足条件的三位数（15 分）
#本题要求实现一个函数，统计给定区间内的三位数中有两位数字相同的完全平方数（如144、676）的个数。
import math
def search(n):
    count = 0
    for index in range(101, n+1):
        low = index % 10
        middle = index // 10 % 10
        high = index // 100
        if low == middle or middle == high or low == high:
            s = str(math.sqrt(index))
            s1 = s.split(".")
            # split返回列表，元素类型为str
            if s1[1] == '0':
                   count += 1
    return count

print(search(500))

# 小结：
# str.split()返回列表，元素为str

#习题10-2 递归求阶乘和（15 分）
#本题要求实现一个计算非负整数阶乘的简单函数，并利用该函数求 1!+2!+3!+...+n! 的值。
#函数fact应返回n的阶乘，建议用递归实现。
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

#函数factsum应返回 1!+2!+...+n! 的值。题目保证输入输出在双精度范围内。
def factsum(n):
    sumResult = 0
    for index in range(1, n+1):
        sumResult += fact(index)
        
    return sumResult

a = int(input())
result = fact(a)
print("fact(%d) = %d" % (a, result))
print(factsum(a))

#习题10-3 递归实现指数函数（15 分）
#本题要求实现一个计算x**​n（n≥1）的函数
#函数calc_pow应返回x的n次幂的值。建议用递归实现。题目保证结果在双精度范围内。
def calc_pow(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * calc_pow(x, n - 1)
    
x = float(input())
n = int(input())

print(calc_pow(x, n))

#习题10-4 递归求简单交错幂级数的部分和（15 分）
#本题要求实现一个函数，计算下列简单交错幂级数的部分和：
def fnx(x, n):
    if n <= 0:
        return
    if n == 1:
        return x
    else:
        return fnx(x, n - 1) + ((-1) ** (n - 1)) * (x ** n)

x = float(input())
n = int(input())

print("%.2f" % fnx(x, n))

#习题10-5 递归计算Ackermenn函数（15 分）
#本题要求实现Ackermenn函数的计算，其函数定义如下：
#其中m和n是用户传入的非负整数。函数Ack返回Ackermenn函数的相应值。题目保证输入输出都在长整型
def ack(m, n):
    if m < 0 and n < 0:
        return
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
print(ack(2, 3))

#习题10-6 递归求Fabonacci数列（10 分）
#本题要求实现求Fabonacci数列项的函数。Fabonacci数列的定义如下：
def fabonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fabonacci(n - 2) + fabonacci(n - 1)
    
print(fabonacci(6))


#习题10-7 十进制转换二进制（15 分）
#本题要求实现一个函数，将正整数n转换为二进制后输出。
#函数dectobin应在一行中打印出二进制的n。建议用递归实现。
def dectobin(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 

def dectobin2(n):
    list1 = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        while (n // 2) != 1:
            list1.append(n % 2)
            n = n // 2
        list1.append(1)
    return "".join(list1)

print(dectobin2(9))
