# -*- coding: utf-8 -*-
"""
Created on Fri May 18 15:43:03 2018

@author: Administrator
"""

# numpy 字符串
# add：连接
import numpy as np
add = np.char.add(["hello"], ["geyang"])
print(add)

# multiply
multiply = np.char.multiply('hello', 3)
print(multiply)

# 首字母大写
capitalized = np.char.capitalize("hello world!")
print(capitalized)

# 分割
split = np.char.split("hello how are you?") # split 默认情况，以空格作为分隔符
print(split)

split2 = np.char.split("nihao geyang, wo shi mama!", sep = ",")
print(split2)

# 分隔符连接
joinStr = np.char.join(":", "dmy")
print(joinStr)

# numpy算术函数
# 三角函数
import numpy as np
a = np.array([0, 30, 45, 60, 90])
print(np.sin(a*np.pi/180))
print(np.cos(a*np.pi/180))

# 四舍五入函数
b = np.array([1.232, 5.55, 1213, 0.567])
print(np.around(b, decimals = 2))


# numpy 算术运算
import numpy as np
inputArray1 = np.arange(9, dtype= np.float).reshape(3,3)
print("第一个数组：", inputArray1)

inputArray2 = np.array([10,10,10])
print("第二个数组：", inputArray2)
# add subtract multiply divide
print(np.add(inputArray1, inputArray2))  # 广播机制
print(np.subtract(inputArray1, inputArray2))

# 返回元素的倒数
# np.reciprocal()

# numpy 统计函数
# np.amin() np.amax() 从数组中给定的元素中查找最小、最大值

# numpy percentile()
#百分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比。 函数numpy.percentile()接受以下参数。
#
#numpy.percentile(a, q, axis)

# numpy.median() 中值
# numpy.mean() 数组的算术平均数
# numpy.average() 加权平均值
# numpy.std()    标准差**2 = 方差 numpy.var()