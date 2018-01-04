# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# # 演示使用list
# # 初始化list
# classmates = ['geyang', 'nihao']
# # 在list末尾添加一个元素
# classmates.append("last")
# # 在list末尾删除一个元素, 或者指定位置元素pop(index)
# classmates.pop()
# 
# # insert插入一个元素， insert(index, element)
# classmates.insert(0, "zero")
# =============================================================================


# 演示使用tuple
tuple1 = ("geyang", "nihao", ["zero", "one"])
tuple2 = (1,20)
#tuple1[0] = "nihao" #TypeError: 'tuple' object does not support item assignment
tuple1[2][0] = "change"