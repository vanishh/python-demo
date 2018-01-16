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
    
    # 如果变量名以__开始，就变为私有变量
    # 在python中，变量名形如__xxx__是特殊变量
    # 特殊变量可以直接访问
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def set_name(self, name):
        self.__name = name
    
    def set_score(self, score):
        if 0 <= score and score <= 100:
            self.__score = score
        else:
            raise ValueError("bad score")
    # 类中的函数，第一个参数永远是实例变量self，
    # 调用时，不用传递该参数，其余与普通函数相同
    def print_score(self):
        print("%s: %s" %(self.__name, self.__score))
    
    def get_grade(self):
        print("self parameter! %s" % self)
        if(self.__score >= 90):
            self.__grade = "excellent"
        elif(self.__score >= 80):
            self.__grade = "good"
        elif(self.__score >= 60):
            self.__grade = "medium"
        else:
            self.__grade = "not pass"
        print(self.__grade)

geyang = Student("geyang", 50)

# 'Student' object has no attribute 'name'
#print(geyang.name)
geyang.set_score(70)
geyang.print_score()
# 可以动态的给对象绑定属性
geyang.address = "shanghai"
print(geyang.address)

geyang.get_grade()
#geyang.set_score(-1) # ValueError: bad score