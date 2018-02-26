# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:43:06 2018

@author: Administrator
"""
'''
copy and deep copy
'''
a = [1, 2, 3]
b = "geyang"
c = True
list1 = [a, b ,c]

# python中，对象的赋值为 对象引用（内存地址）的传递
list2 = list1
# id() 获取变量在内存中的地址
# list1 和 list2 地址相同，指向相同对象
print(id(list1))
print(list1)
print([id(ele) for ele in list1])

print(id(list2))
print(list2)
print([id(ele) for ele in list2])

list1[0].append(4)
# 地址任然相同
print(id(list1))
print(list1)
print([id(ele) for ele in list1])

print(id(list2))
print(list2)
print([id(ele) for ele in list2])

# 浅拷贝
import copy
 
will = ["Will", 28, ["Python", "C#", "JavaScript"]]
# 使用copy模块里的浅拷贝copy函数
# 浅拷贝创建新的对象赋值给wilber变量
wilber = copy.copy(will)
 
print( id(will))
print( will)
print( [id(ele) for ele in will])

# 对于新对象中的元素，浅拷贝使用原始元素的引用（内存地址）
print( id(wilber))
print( wilber)
print( [id(ele) for ele in wilber])
 
will[0] = "Wilber"
will[2].append("CSS")
print( id(will))
print( will)
print( [id(ele) for ele in will])
print( id(wilber))
print( wilber)
print( [id(ele) for ele in wilber])

# 测试切片
listTest = [1, 2, 3, 4]
listSlice = listTest[:]
print(id(listTest))
print(listTest)
print([id(ele) for ele in listTest])

print(id(listSlice))
print(listSlice)
print([id(ele) for ele in listSlice])

# 修改源列表
listTest[0] = 5
print(id(listTest))
print(listTest)
print([id(ele) for ele in listTest])

print(id(listSlice))
print(listSlice)
print([id(ele) for ele in listSlice])


# 小结
# 浅拷贝创建新变量，新变量中的元素使用原始元素的引用（内存地址）
# 当使用以下操作时，会产生浅拷贝效果
# 切片[:]、工厂函数list()/set()、copy模块的copy函数、dict的copy函数

# 深拷贝
import copy
 
will = ["Will", 28, ["Python", "C#", "JavaScript"],(1,)]
                     
# 使用copy模块的deepcopy函数进行深拷贝
# 创建一个新对象
wilber = copy.deepcopy(will)

# 新对象中，对象中的元素，深拷贝都会重新生成一份（有特殊情况：对于不可变类型，还是使用原始元素的引用），
# 而不是使用原始元素的引用（内存地址）
print( id(will))
print( will)
print( [id(ele) for ele in will])
print( id(wilber))
print( wilber)
print( [id(ele) for ele in wilber])
 
will[0] = "Wilber"
will[2].append("CSS")
print( id(will))
print( will)
print( [id(ele) for ele in will])
print( id(wilber))
print( wilber)
print( [id(ele) for ele in wilber])