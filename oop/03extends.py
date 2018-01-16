# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:36:38 2018

@author: Administrator
"""

class Animal(object):
    def run(self):
        print("Animal is running ...")

class Dog(Animal):
#    pass
    # 子类覆盖父类run()方法
    def run(self):
        print("Dog is running ...")

class Cat(Animal):
    def run(self):
        print("Cat is running ...")

def run_twice(animal):
    animal.run()

dog1 = Dog()
dog1.run()

animal = Animal()
animal.run()
print(isinstance(animal, Animal))
print(isinstance(animal, Dog))

# 父类引用指向子类对象
animal = Dog()
# 实现多态
animal.run()
print(isinstance(animal, Animal))
print(isinstance(animal, Dog))

run_twice(animal)

cat1 = Cat()
run_twice(cat1)