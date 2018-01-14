# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# partial 偏函数
# functools.partial函数 用来给一个函数的某些参数设置默认值，以方便调用

import functools

# 使用partial函数给函数设置参数默认值，返回一个新函数
int2 = functools.partial(int, base = 2)

# 调用新函数会使用默认参数值
print(int2('1000001'))

# 小结
# 当函数参数太多，需要简化时使用partial函数固定原函数的某些参数，生成调用简单的新函数
