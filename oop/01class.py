# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 00:32:13 2018

@author: Administrator
"""
# 在python中，所有的数据类型都可以视为对象
# 也可以自定义一个对象
# 定义类：class 类名(继承自某类)
# object类，所有类最终都会继承该类
class Student(object):
    
    # 通过定义一个特殊的__init__()方法，在创建实例的时候，把name、score 等属性绑定上去
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    # 类中的函数，第一个参数永远是实例变量self，表示指向创建的实例本身
    # 调用时，不用传递该self参数，其余与普通函数相同
    # self 不是python关键字，也可以使用其他参数名代替self，推荐使用self
    def print_score(self):
        print("%s: %s" %(self.name, self.score))
    
    def get_grade(self):
        print("self parameter! %s" % self)
        if(self.score >= 90):
            self.grade = "excellent"
        elif(self.score >= 80):
            self.grade = "good"
        elif(self.score >= 60):
            self.grade = "medium"
        else:
            self.grade = "not pass"
        print(self.grade)

geyang = Student("geyang", 50)
print(geyang.name)
geyang.print_score()
# 可以动态的给对象绑定属性
geyang.address = "shanghai"
print(geyang.address)

geyang.get_grade()

class Animal():
    
    name = "geyang"
    count = 0
    # python 中不支持函数的重载，类中函数名相同的函数只有一个
    def __init__(self):
        print("constructor function")
        Animal.count += 1
        
    def print_fun(self):
        print("print")

# 创建对象时，首先调用构造函数
animal = Animal()
print(animal.count)
animal1 = Animal()
print(animal1.count)
# 调用成员函数时，必须在定义成员函数时提供一个参数；没有定义参数，也可以执行通过
animal.print_fun()
print(animal.name)

class Dog(Animal):
    
    def __init__(self):
        print("sub constructor function!")
        
dog = Dog()