# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 00:36:19 2018

@author: Administrator
"""
# python可以动态的给对象或者类绑定属性和方法
# 给对象绑定的属性和方法 只属于当前对象
# 给类绑定的属性和方法 属于类
class Student(object):
    
    # 可以在class中定义属性，这种属性属于类属性，属于Student类
    height = 172
    
    # 统计对象创建的次数
    count = 0
    
    # 可以给实例绑定任何属性和方法，动态语言的灵活性
    def __init__(self, name):
        self.name = name
        Student.count += 1
        
s = Student("geyang")
#person1 = Person("nihao")
# 给实例绑定属性，只属于当前实例
# 注意：不要对实例属性和类属性使用相同的名字 相同名称的实例属性名将屏蔽类属性

s.score = 90 # 动态绑定实例属性
print(s.name)

print("class height:", Student.height) # height为类属性名
print("object height:", s.height)
person1 = Student("nihao")
print(person1.name)


# 之前演示给对象绑定属性
# 还可以给对象或类绑定方法

def setAge(self, age):
    self.age = age

student1 = Student("geyang")
student1.setAge = setAge # 给student1动态绑定setAge方法
student1.setAge(student1, 10) # 调用setAge(传入两个参数)
print(student1.age)

student2 = Student("qingqing")
#student2.setAge(student2, 100) #AttributeError: 'Student' object has no attrib