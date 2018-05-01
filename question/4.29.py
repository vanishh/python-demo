# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 00:51:47 2018

@author: Administrator
"""


from collections import Iterable
document = open("test.txt", "w+")
isinstance(document, Iterable)

def test():
    print("test")
    
print(test())

def isPrime(n):
    for index in range(2,n):
        if (n % index) == 0:
            return False
    return True

def printPrim():
    list1 = ""
    count = 0
    line = 1
    for index in range(100, 301):
        if count == 8:
            print(list1)
            print("----"+str(line)+"----")
            list1 = ""
            count = 0
            line += 1
        if isPrime(index) == True:
            list1 += " " + str(index)
            count += 1
            
printPrim()