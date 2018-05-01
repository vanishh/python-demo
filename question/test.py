# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 00:09:49 2018

@author: Administrator
"""

def isPrime(n):
    for index in range(2,n):
        if (n % index) == 0:
            return False
    return True

def printPrim():
    list1 = ""
    count = 0
    line = 1
    for index in range(100, 301):
        if count == 8:
            print(list1)
            print("----"+str(line)+"----")
            list1 = ""
            count = 0
            line += 1
        if isPrime(index) == True:
            list1 += " " + str(index)
            count += 1
            
printPrim()


def printLevel(n):
    line = ""
    for index in range(n):
        line = line + " " + str(2 ** index)
    for index in range(n-2,-1, -1):
        line = line + " " + str(2 ** index)
    return line
    
#printLevel(4)
def printPrimid():
    for index in range(9):
        line = printLevel(index)
        print(" " * 2*(9 - index) + line + "\n")
printPrimid()


def checkList(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            if i == j:
                result.append(j)
                
    if len(result) == 0:
        return True
    else:
        return result
    
list1 = [1,2,3]
list2 = [2, 4, 5]
print(checkList(list1, list2))


class NumberException(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo
    

def getGCD(number1, number2):
    if (number1 % number2 == 0):
        return number2
    else:
        return getGCD(number2, number1 % number2)
        
#print(getGCD(10, 23))
        
def checkCommonDivisor():
    try:
        int1 = int(input())
        int2 = int(input())
        if (int1 < 1 or int1 > 1000) or (int2 < 1 or int2 > 1000 ):
            raise NumberException("输入数据异常")
        print(getGCD(int1, int2))
    except NumberException as e:
        print(e)
        
checkCommonDivisor()
    

# 求一元二次方程实数根、
# b**2 - 4ac >= 0 时，有实数根
import math
def checkFunction():
    inputStr = input("请输入a,b,c(格式：a,b,c):")
    inputList = inputStr.split(",")
    temp = int(inputList[1]) ** 2 - 4 * int(inputList[0]) * int(inputList[2])
    if temp >= 0:
        x1 = (-1 * int(inputList[1]) + math.sqrt(temp)) / (2 *int(inputList[1]))
        x2 = (-1 * int(inputList[1]) - math.sqrt(temp)) / (2 * int(inputList[1]))
        print("方程有实数根, x1=%s, x2=%s" % (x1, x2))
    else:
        print("方程没有实数根")
        
checkFunction()


def factorial(n):
    result = 1
    for index in range(1, n+1):
        result *= index 
    return result
print(factorial(4))

def sumFactorial(n):
    sum = 0
    message = ""
    for index in range(1, n+1):
        message = message + "+" + str(index) + "!"
        sum += factorial(index)
    message += "=%s"
    print(message[1:] % sum)
    
sumFactorial(3)

# 编写矩形类
class Rectangle(object):
    def __init__(self, width, length):
        self.__width = width
        self.__length = length
    
    def get_width(self):
        return self.__width
    
    def get_length(self):
        return self.__length
    
    def area(self):
        return self.__length * self.__width
    
r = Rectangle(10, 3)
print("矩形面积：", r.area())

class Cuboid(Rectangle):
    
    def __init__(self, width, length, height):
        super(Cuboid, self).__init__( width, length)
        self.__height = height
        
    def volumn(self):
        return self.__height * super(Cuboid, self).get_length() * super(Cuboid, self).get_width()
    
    def under_area(self):
        return super(Cuboid, self).get_length() * super(Cuboid, self).get_width()
    

cub = Cuboid(10,3, 2)
print("长方体体积：", cub.volumn())
print("底面积：", cub.under_area())


class Person(object):
    def __init__(self, name, sex, age, nation):
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__nation = nation
        
    def eat(self):
        print("%s在吃饭" % self.__name)
    def sleep(self):
        print("%s在睡觉" % self.__name)
    def work(self):
        print("%s在工作" % self.__name)
        
    def get_name(self):
        return self.__name
   
geyang = Person("geyang", "man", 24, "china")     
geyang.eat()
class Student(Person):
    def __init__(self, name, sex, age, nation, school, schoolId):
        super(Student, self).__init__( name, sex, age, nation)
        self.__school = school
        self.__schoolId = schoolId
        
    def work(self):
        print("%s的工作是学习" % super(Student, self).get_name())
        

lixiang = Student("lixiang", "man", 30, "china", "ncepu", 1234)
lixiang.work()

class StudentLeader(Student):
    def __init__(self, name, sex, age, nation, school, schoolId, title):
        super(StudentLeader, self).__init__( name, sex, age, nation, school, schoolId)
        self.__title = title
        
    def hold_meeting(self):
        print("%s正在开会" % super(StudentLeader, self).get_name())
        
studentLeader = StudentLeader("张三", "男", 30, "中国", "北大", 12345, "学习委员")
studentLeader.hold_meeting()

    