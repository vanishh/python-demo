# -*- coding: utf-8 -*-
"""
Created on Sat May 19 11:46:35 2018

@author: Administrator
"""

# numpy 包含一个matrix库 numpy.matlib 
# 此模块的函数返回矩阵而不是返回ndarray对象
# 矩阵总是二维的，ndarray 可以是n维
import numpy.matlib
import numpy as np
matrix = np.matrix("1,2;3,4")
print(matrix)
print(np.matlib.empty((2,2)))
print(np.matlib.zeros((2,2)))
print(np.matlib.ones((2,2)))
# 对角线元素为1，其他位置为0
print("对角矩阵：", np.matlib.eye(n = 4, M = 4, k = 0, dtype= float))
# 单位矩阵
print("单位矩阵:", np.matlib.identity(5, dtype = float))
# 随机值矩阵
print("随机值矩阵：", np.matlib.rand(3,3))


# numpy.linalg 模块
# 提供线性代数所需的所有功能：点积、内积、矩阵积、行列式、求解线性矩阵方程

import numpy.matlib
import numpy as np 
a = np.array([[1,2],[3,4]])
print("a:", a)
b = np.array([[11,12],[13,14]])
print("b", b)
# np.dot 
print("数组点积:", np.dot(a,b)) # 返回两个数组的点积，对于二维向量，其等效于矩阵乘法
# np.vdot : 返回两个向量的点积
print("向量点积：", np.vdot(a,b))
# np.inner ：返回一维数组的向量内积
print("向量内积：", np.inner(np.array([1,2,3]), np.array([0,1,0])))

# numpy.linalg.solve()函数给出矩阵形式线性方程组的解
# numpy.linlg.inv() 计算矩阵的逆