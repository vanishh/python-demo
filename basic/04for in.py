# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# for in
#names = ["geyang", "nihao", 15, True]
#
#for name in names:
#    print(name)
#
## 计算1到1000的和
#list1 = list(range(101))
#sum = 0
#for x in list1:
#    sum = sum + x
#print(sum)

# while
#sum = 0
#n = 1
#while n <= 100:
#    sum = sum + n
#    n = n + 1

# break 结束当层循环，不能结束外层循环
#n = 1
#k = 1
#while n < 10:
#    while k < 20:
#        if n == 3:
#            break
#        
#        print("%s:%s" % (n, k))
#        k = k + 1
#    n = n + 1
#    k = 1
#    
#print("END")

# continue 跳过本次循环
# 注意本例中 使用while循环不能实现想要效果
index = 1
while index < 10:
    if index == 5:
        continue
    print(index)
    index = index + 1
    
print("END")

