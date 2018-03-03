# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:48:37 2018

@author: Administrator
"""

# 数据结构起步能力自测题
# 自测1
# 把给定的符号打印成漏斗形状
#*****
# ***
#  *
# ***
#*****


# 自测2
# 定义dn = p(n+1) - p(n), 其中p(i)是第i个素数，显然有d1 =1,且对于n > 1，有dn是偶数。
# 素数对猜想认为"存在无穷多对相邻且差为2的素数" 
# 现给定任意正整数N ，N 小于10**5，计算不超过N的满足猜想的素数对个数

# 判断一个数是否非素数
import math
def is_prime(number):
    end = math.ceil(math.sqrt(number))
    for index in range(2, end+1):
        if number % index == 0:
            return False
    return True

#print(is_prime(5))

# 获得小于n的素数
def count_prime(n):
    result = []
    for number in range(2,n+1):
        if is_prime(number) == True:
            result.append(number)
            
    return result

#print(count_prime(20))

# 获得满足素数对猜想的素数对及个数
def count_prime_pair(n):
    prime = count_prime(n)
    count = 0
    for index in range(len(prime)-1):
        if (prime[index] - prime[index + 1]) ==  -2:
            count += 1
    return count

#print(count_prime_pair(20))
if __name__ == "__main__":
    number = int(input())
    print(count_prime_pair(number))

# 自测3数组元素循环右移问题
#一个数组A中存有N（>0）个整数，在不允许使用另外数组的前提下，将每个整数循环向右移M（≥0）个位置，
#如将012345，右移2位，变为450123（最后M个数循环移至最前面的M个位置）。如果需要考虑程序移动数据的次数尽量少，要如何设计移动的方法？

# 参数list1 :表示传入移动数据，n:右移几位
# 返回值：字符列表
def shift(list1, n):
    if not isinstance(list1, list):
        list1 = list(list1)
    for index in range(n):
        last = list1.pop()
        list1.insert(0, last)
    return list1

list1 = [1,2,3,4]
print(shift(list1, 2))

def main_shift():
    input_args = input()
    input_list = input_args.split(" ") # split() 返回字符列表
    input_number = input()
    number_list = input_number.split(" ")
    result = shift(number_list, int(input_list[1]))
    print(result)
    line = ""
    for index in range(len(result)):
        if index == (len(result) - 1):
            line = line + str(result[index])
        else:
            line = line + str(result[index]) + ' '
    print(line)
    
main_shift()
    
            
# 1. str类型的split()方法，返回字符列表
                
                
            