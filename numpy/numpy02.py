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


# numpy