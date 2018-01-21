# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# dict key-value 数据类型
# key 唯一对应一个 value(1 对 1)
# key 必须为不可变对象，如字符串等
dict1 = {"geyang": 100, "bob": 99, "gavin": 95, 101:101}

# 访问字典
print(dict1["geyang"])
print(dict1[100])
# 添加字典对
dict1["nihao"] = 60 # 添加一个key-value
dict1["nihao"] = 80

# 删除字典对
# value = dict1.pop(key)
result = dict1.pop("bob")

# dict常用函数
# key in dict
if "geyang" in dict1:
    print(dict1["geyang"])
    print(dict1.get("geyang"))
else:
    print("geyang is not in dict1")
    
keys = dict1.keys()

values = dict1.values()

for k, v in dict1.items():
    print(k, '=', v)

# 字典练习
# 创建多个字典 放在列表中， 遍历列表 打印数据
dog = {"type":"hasky", "master":"geyang"}
cat = {"type":"bosi", "master":"geyang"}
pets = [dog, cat]

for element in pets:
    if "type" in element:
        print("type:%s" % element["type"])
    if "master" in element:
        print("master:%s" % element["master"])

# set 无序、不重复的集合
# set 底层原理与dict 相同，没有value，不能存入可变对象
test = set([1,2,3])
test.add(4)
test.remove(1)

test2 = set([2,3,5])

# 并集
union = test | test2 

#交集
common = test & test2



# 不可变对象
list1 = [1,2] # 可变对象类型  TypeError: unhashable type: 'list'
str1 = "test" # 不可变对象类型
int1 = 10 # 不可变对象
tuple1 = (1, 2, 3) # 不可变对象
tuple2 = (1, [2, 3]) # 有问题，不能hash tuple2 TypeError: unhashable type: 'list'
dict1 = {tuple2 : "test"} # 


