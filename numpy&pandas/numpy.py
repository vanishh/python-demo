# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:51:38 2018

@author: Administrator
"""
# Numpy 构造函数
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# dtype : 数组所需的数据类型
# copy : 对象是否被复制
# order : 排序方式
# ndmin : 指定返回数组的最小维度
# Numpy 的运算单位 数组
# 数组的算数和逻辑运算
# 傅里叶变换
# 与线性代数有关的操作

# 导入numpy
import numpy as np

# 创建ndarray 一个维度 
a = np.array([1,2,3])
print(a)

# 两维的ndarray
b = np.array([[1,2],[3,4]])
print(b)

c = np.array([1,2,3,4,5], ndmin = 3)
print(c)

d = np.array([1,2,3], dtype = np.complex)
print("complex:", d)
print(d.flags)

# np.arange(start, stop, step, dtype) 来自数值范围的数组
arange = np.arange(1, 24, 2, dtype = np.float)
print("arange:", arange)

# np.linspace(start, stop, num数组要生成的个数, endpoint 数组中是否包含stop值)
linspace = np.linspace(10, 20, 5, endpoint = False)
print("linspace:", linspace)

# np.logspace() 返回一个ndarray对象
# np.zeros 默认为float类型
zeros = np.zeros(5, dtype = np.int)
print("zeros:", zeros)

zeros1 = np.zeros(5)
print("zeros:", zeros1)

onesArray = np.ones(5)
print("ones:", onesArray)

# 使用现有数据创建数组
asArray = np.asarray([1,2,3,4], dtype = np.float)
print("as array:", asArray)

# NumPy数字类型是dtype 对象的实例
# NumPy的属性: shape reshape ndim itemsize
# shape reshape
shapeArray = np.array([[1,2,3],[4,5,6]])
print(shapeArray.shape) # (2,3) 两行三列

reshape = np.array([[1,2,3],[4,5,6]])
reshape.shape = (3,2) # 改为三行两列
print(reshape)

# ndim 数组的维数
arange = np.arange(24)
print(arange)
print(arange.ndim) # ndim 表示维数
# numpy.itemsize 返回数组中每个元素的字节单位长度
print(arange.itemsize)
arange1 = arange.reshape(2,4,3)
print(arange1)

# Numpy 切片和索引
# ndarray 对象的内容可以通过索引或者切片来访问或者修改
# 三种索引方法类型：字段访问、基本切片、高级切片
a = np.arange(10)
print(a)
print(a[5])
print(a[2:7:2])
print(a[2:])

np.array([[1,2,3], [3,4,5], [4,5,6]])
# 基本切片 python 中切片的概念扩展到n维

# 高级索引
# 高级索引始终返回数据的副本
# 两类高级索引：整数、布尔值
# 整数索引

# 布尔索引
a = np.array([[1,2,3], [2,3,4], [3,4,5]])
print(a)
print(a[ a > 3])

nanArray = np.array([np.nan, 1, 2, np.nan,3, 4])
print(nanArray)
print(nanArray[~np.isnan(nanArray)])


# Numpy 广播
# 广播是指numpy 在算术运算期间处理不同形状数组的能力

# 如果阵列的形状相同，操作被无缝执行
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
print(a * b)

# 广播
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])
print(a)
print(b) 
print(a + b)

# 数组上的迭代
a = np.arange(0,60,5)
#print(a)
a = a.reshape(3,4)  # 生成3*4的二维数组
#print(a)

# 遍历数组
#for x in np.nditer(a):
#    print(x)

# 矩阵的转置
b = a.T
print(b)








 
