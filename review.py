# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:34:54 2018

@author: Administrator
"""

# 容器的操作
tuple1 = (1, 2, 3)
# 访问 
print(tuple1[:])
print(tuple1[0])
del(tuple1[0]) # tuple中元素不可改变
del(tuple1)

str1 = "test"
print(str1[:])
print(str1[0])
del(str1[0])

list1 = [1, 2, 3]
print(list1[:])
print(list1[0])
del(list1[0])
# 添加元素
# 元组不可以被修改，包括添加元素，任何方法都不可以
#tuple1[3] = 4 # 'tuple' object does not support item assignment
#list1.append(5)

#修改元素
#tuple1[0:1] = 0 # 元组切片不可以
#tuple1[0] = 0 # 元组索引不可以

#list1[0:2] = [0] # 列表切片可以
#list1[0] = 0 # 列表索引可以

#str1[0:2] = '0' #不可以
#str1[0] = '0'    #不可以

# 小结：
# 1.str、元组、列表可以进行切片操作，可以索引访问
# 2.元组不可以被修改，包括添加元素、修改原有元素；任何方法都不可以（包括切面、索引）
# 3.str不可以被修改，索引、切片都不可以

print("ddd22".isalnum())  # True
print("mm".isalpha())     # True
print("mm334".isalpha())  # False
print([1,2,3].count(4))   # 0 ???

dict1 = {"name":"geyang", "age":24, "height":173}
#dict1["weight"] = 70 # 增
#del(dict1["name"])   # 删
#dict1["weight"] = 80 # 改
#print(dict1["weight"]) # 查

keys = dict1.keys()
print(keys)
values = dict1.values()
print(values)
print(dict1.get("name"))
print(dict1.get("name1")) # get()方法，如果查找键不存在，返回None
items = dict1.items()
print(items)
#dict_items([('name', 'geyang'), ('age', 24), ('height', 173)])

a = 0
while a < 2:
    print("a = %d" % a)
    a += 1
else:
    print("test")

# 小结：
# for 和 while 可以搭配else语句
    
list2 = [5, 2, 8]
result = list2.sort() # sort()方法没有返回值,直接对list进行排序
print(list2)
print(list2[-1])

#考试题1 小明和女朋友买士力架吃，每天小明吃1个，女朋友吃半个，
# 直到第6天时，剩下1个。问小明买了几个?
# 分析：count(6) = 1 count(5) = count(6) + 1.5 求count(1)
# count(n) = count(n + 1) + 1.5
def count(day):
    if day == 6:
        return 1
    else:
        return count(day + 1) + 1.5


print(count(1))
        
# 考试题2：一次性输入任意不少于5个数字（数字之间以逗号为界）保存在list中，
# 对输入的数字进行排序，不准使用内置函数，封装成函数
def sort_number():
    input_str = input()
    number_list = input_str.split(",")
#    print(number_list)
    number_list = [ int(index) for index in number_list]
    print("before sort:", number_list)
    # 冒泡排序
    bubble_sort(number_list)
    print("after sort:", number_list)
    
def bubble_sort(number_list):
    for j in range(1, len(number_list)):
        for i in range(len(number_list) - j):
            if number_list[i] > number_list[i+1]:
                # 交换
                temp = number_list[i+1]
                number_list[i + 1] = number_list[i]
                number_list[i] = temp

# 测试
#number_list = [5, 3, 8, 1]
#bubble_sort(number_list)

sort_number()

# 考试3：切割列表元素，如果相邻元素相同，则切割存放在一起，不同则单独切割
# 封装为函数
def slice_list():
    temp_list = []
    result_list = []
    index = 0
    input_list = [1, 1, 0, 2, 2, 2, 4, 3, 3, 4, 2, 0, 0]

    while True:
        if index == len(input_list):
            break
        while input_list[index] == input_list[index+1]:
            temp_list.append(input_list[index])
            index += 1
        temp_list.append(index)
        result_list.append(temp_list)
        index += 1
    
    
slice_list()

# 考试题4：写一个程序，可以任意输入文件名，打开该文件，如果文件不存在则创建该文件。
# 然后输入内容，可重复输入追加到文件中。

# 考试题5：计算年龄
#f(1) = 10 f(2) = f(1) + 2 f(3) = f(2) + 2
def count_age(number):
    if number == 1:
        return 10
    else:
        return count_age(number -1) + 2
    
print(count_age(5))

# 考试题6：time操作
# (1)将字符串的时间"2017-12-31 23:24:00" 转为时间戳和时间元组
# (2)字符串格式更改
# (3)获取两天前的时间
# (4)通过time输出时间
import time

time_format = "2017-12-31 23:24:00"
# (1)转为时间戳
timestamp = time.mktime(time.strptime(time_format, "%Y-%m-%d %H:%M:%S"))
print(timestamp)
# 转为时间元组
localtime = time.localtime(timestamp)
print(localtime)

# (2)格式修改
time_format1 = time_format.replace("12", "10")
time_format1 = time_format1.replace("31", "10")
print(time_format1)


timestamp = time.mktime(time.strptime(time_format1, "%Y-%m-%d %H:%M:%S"))
localtime = time.localtime(timestamp)
time1 = time.strftime("%Y/%m/%d %H-%M-%S", localtime)
print(time1)

# (3)获取前两天的时间
# 使用datetime 模块
import datetime
now_time = datetime.datetime.now()
print(now_time)

yesterday = now_time + datetime.timedelta(days=-2)
print(yesterday)

formated_yesterday = yesterday.strftime("%Y-%m-%d %H:%M:%S")
print(formated_yesterday)

# (4)通过time输出时间
time_format_4 = "2018-01-01 08:08:08"
timestamp4 = time.mktime(time.strptime(time_format_4, "%Y-%m-%d %H:%M:%S"))
localtime4 = time.localtime(timestamp4)
print(localtime4)
time4 = time.strftime("今天是%Y年%m月%d日 %H点%M分%S秒", localtime4)
print(time4)

#考试题7 定义一个班级类
class Class(object):
    
    __person_number = 0
    
    def __init__(self, person_number):
        Class.__person_number = person_number
    
    def increase_person_number(self):
        pass
    
    def get_peson_number(self):
        return Class.__person_number
    
class Student(Class):
    
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_score(self, class_name):
        if class_name in self.score:
            return "%d:%d" % (class_name, self.score[class_name])