# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#
## 注意 input返回的结果为str类型，str 不能和数字进行比较，需要转换为int
#s = input("请输入年龄:")
#age = int(s)
#if age >= 18:
#    print("your age is %s" % age)
#    print("adult")
#elif age >= 6:
#    print("teenager")
#else:
#    print("kid");
    
# 例2 计算BMI = weight / (height * height)
height = 1.73
weight = 70

bmi = 80.5 / (1.75 ** 2)

if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")
