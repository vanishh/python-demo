# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 如果函数写在文件中 使用 from fimename import fun_name
import math
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

n = my_abs(-10)
print(n)

# 返回多个值 本质是返回一个tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


# 位置参数举例 
def power(x, n):
    result = 1
    while n > 0:
        result = result * x
        n = n - 1
    return result

result1 = power(10, 3)

# 默认参数
# 定义函数时可以提供默认参数值
# 调用函数时，如果有默认参数，可以不用提供参数

def enroll(name, gender, age=6, city="beijing"):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)
    
enroll("geyang", "man")
enroll("ligang", "women", city="tianjing", age = 15) # 提供参数位置应对应 若位置不对应，调用时应写上参数名=value

# 默认参数 指向可变对象
# 当调用提供参数时，没有问题； 不提供参数，结果累加？？
# 牢记：默认参数必须指向不可变对象

# 'NoneType' object has no attribute 'append'
def add_end(list1=None):
    if list1 is None:
        list1 = []
    list1.append("END")
    return list1

print(add_end(["geyang"]))

# 可变参数 
# 定义的函数，传入的参数的个数是不确定的，可变的
# 可变参数在函数调用时自动组装为一个tuple
def addAll(*numbers):
    result = 0
    for element in numbers:
        result += element **2
    return result

# 练习：位置参数、可变参数、多个返回值
def calc(name, *numbers):
    sum = 0;
    name = "change"
    for element in numbers:
        sum = sum + element ** 2
    return name, sum
# 调用方式1：传入可变的参数个数
resultAsName, resultAsNumbers = calc("geyang", 1, 2, 3)

print("name:", resultAsName, "sum:", resultAsNumbers)

# 调用方式2：传入一个list 
listTwo = [1, 2, 3]
print(calc("nihao", *listTwo))

# 关键字参数
# 关键字参数允许你传入可变的含参数名的参数 
# 关键字参数在函数内自动组装为一个dict

def person(**kw):

    # 我们可以在函数内部查看传了哪些参数
    if "city" in kw:
        print("city:", kw["city"])
    elif "job" in kw:
        print("job:", kw["job"])
    else:
        print("other:", kw)
        
person(job = "engineer", language = "java")


#person(language = "java")
# 命名关键字参数
#如果要限制关键字参数的名字， 需要使用命名关键字参数
# 调用命名关键字参数时，参数命名一致，位置一致，个数一致
def person(*, city, job):
    print(city)
    print(job)

person(city="geyang", job="engineer")