# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:43:32 2018

@author: Administrator
"""
#习题6-1 分类统计字符个数（15 分）
#本题要求实现一个函数，统计给定字符串中英文字母、空格或回车、数字字符和其他字符的个数。
def stringCount(inputStr):
    blankCount = 0
    alphaCount = 0
    digitCount = 0
    otherCount = 0
    inputStr = str(inputStr)
    for char in inputStr:
        if str(char) == ' ' or str(char) == '\n':
            blankCount += 1
        elif str(char).isalpha():
            alphaCount += 1
        elif str(char).isdigit():
            digitCount += 1
        else:
            otherCount += 1
    print("letter = %d, blank = %d, digit = %d, other = %d" % (alphaCount, blankCount, digitCount, otherCount))

inputStr = input()
stringCount(inputStr)