# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:28:51 2018

@author: Administrator
"""
# time模块
# Python 提供time 和calendar模块用于格式化日期和时间
# time模块下有很过函数可以转换常见的日期格式
import time

# time.time()获取当前时间戳 时间戳自从1970年1月1日午夜开始的
ticks = time.time()
print("当前的时间戳: %d" % ticks)

# 时间元组
# 用一个元组组装起来的9组数字
# struct_time 元组
localtime = time.localtime(time.time())
print("时间元组：", localtime)

# 格式化时间
# 可以根据需求选取各种格式：time.asctime(时间元组)
asctime = time.asctime(time.localtime(time.time()))
print("本地时间为：", asctime)

# 格式化日期
# strftime(format, time)方法来格式化日期
# 格式化为：2017-12-31 11:45:39 的格式
time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(time1)

time2 = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
print(time2)

time3 = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
print(time3)

# 格式化为：Mon Feb 26 14:10:46 2018
time4 = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
print(time4)

# 将格式字符串转换为时间戳
time_format = "Mon Feb 26 14:10:46 2018"
print(time.mktime(time.strptime(time_format, "%a %b %d %H:%M:%S %Y")))


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