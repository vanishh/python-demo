# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 15:05:54 2018

@author: Administrator
"""

import pandas as pd

# 通过list创建Series
ser01 = pd.Series([1,2,3,4])
print(ser01)
print(ser01.dtype)
print("values:", ser01.values) #获取values属性
print("index", ser01.index)   # 获取index属性

# 通过index属性可以设置索引
ser01.index = ['a','b', 'c', 'd']
print(ser01)

# 通过dict创建Series
# key 变为索引
dict1 = {"a": 11, "b":20, "c":30}
ser02 = pd.Series(dict1)
print(ser02)
print(ser02['a'])
print(ser02[0]) # 虽然索引变为a，但使用0还是可以获取到
print(ser02[0:2]) #使用切片的方式切数据，从0开始，到2,2不要

# Series的运算
ser03 = pd.Series(dict1)
print(ser03 > 15)
print(ser03[ser03 > 15])
print(ser03 + 10)

# numpy 函数可以直接使用pandas数据类型
import numpy as np
print("numpy 开根号：\n", np.sqrt(ser03))

# series 及其索引的name属性
ser04 = pd.Series(dict1)
ser04.name = "test" # 给series name属性设置值
print(ser04)

ser04.index.name = "索引"
print(ser04)

# DataFrame  二维数组
# 通过列表创建
dataFrame01 = pd.DataFrame([["geyang","nihao"],[100, 60]])
print(dataFrame01)

# 通过字典创建
dataFrame02 = pd.DataFrame({
        "name":["geyang", "nihao", "zhaihua"],
        "age": [20, 30,15]
        }, index = ["one", "two", "three"])
print(dataFrame02)

# 获取数据
print("dataFrame02 获取数据：\n", dataFrame02["name"])
# 行获取数据
print("行获取：\n", dataFrame02.loc["one"])
print("行获取：\n", dataFrame02.loc["one", "name"]) # 获取one行，name列的数据

dataFrame02.loc["one"] = [21, "change_one"]

# 从文件中读取数据 read_csv("data.csv")  read_excel()

# 缺省值处理
# df.fillna(0) 所有的NaN用0 填充
# df.fillna(0:1, 1:2) 填充第0列，填1；第1列填2
# df.sum(axis = 0) 参数代表按行或者列求和，参数可省略
# median() 同样，参数代表按行或者列的中位数

# 唯一值 unique()
ser001 = pd.Series(["a", "a", "d", "a"])
resultUnique = ser001.unique()
print(resultUnique)

# isin() 成员资格 判断数据是否在参数中 返回真值列表
resultIn = ser001.isin(["a"])
print(resultIn)

# 选出数据
print(ser001[resultIn])  # 使用布尔索引，取出True对应的值