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
    
    # 通过定义一个特殊的__init__方法，在创建实例的时候，
    # 把name、score 等属性绑定上去
    # __init__第一个参数永远是self:表示指向创建的实例本身
    # 但self不需要传，python会自己把self传进去
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    # 类中的函数，第一个参数永远是实例变量self，
    # 调用时，不用传递该参数，其余与普通函数相同
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