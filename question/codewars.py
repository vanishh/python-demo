# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:40:00 2018

@author: Administrator
"""
# code wars练习
# 三阶斐波那契数列
# 1,1,1,3,5,9...
def tribonacci(signature, n):
    #your code here
    list1 = []
    if n == 0:
        return list1
    for index in range(1,n+1):
        result = tribonacci_at_number(signature, index)
        list1.append(result)
    return list1

def tribonacci_at_number(signature, n):
    if n == 1:
        return signature[0]
    elif n == 2:
        return signature[1]
    elif n == 3:
        return signature[2]
    else:
        return tribonacci_at_number(signature, n - 3) + tribonacci_at_number(signature, n - 2) + tribonacci_at_number(signature, n - 1)
                
signature = [1,1,1]
print(tribonacci_at_number(signature, 5))
print(tribonacci(signature, 7))

# 斐波那契数列
# 1,1,2,3
def fabonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fabonacci(n - 1) + fabonacci(n - 2)
    
print(fabonacci(4))

def test_range():
    for index in range(4): # range(x) : 从0到x-1
        print(index)
test_range()

# beta练习1
# 计算数据的算术平均值和Geometric 平均值
# 例如：一组数据：1， 3， 9， 27， 81
# 算术平均值： (1 + 3 + 9 + 27 + 81) / 5 = 121 / 5 = 24.2
# Geometric平均值：(1 * 3 * 9 * 27 * 81) ^ (1/5) = 9
# 现在给你一组少了一个数据的序列，和序列的算术平均值，求出这个数字和该组数的Geometric平均值
def geo_mean(nums, arith_mean):
    # Your code here:
    number = find_number(nums, arith_mean)
    return geometric_mean(nums, number)
   
def find_number(nums, arith_mean):
    total = 0
    for index in range(len(nums)):
        total += nums[index]
    result = arith_mean * (len(nums) + 1) - total
    return result
 
#list1 = [1,2,3,4,5]  平均值为3
#list1 = [1,2,3,4]
#print(find_number(list1, 3))

def geometric_mean(nums, number):
    # geometric mean
    result = 1
    for index in range(len(nums)):
        result *= nums[index]
    result *= number
    return result ** (1/(len(nums) + 1))
    
#list1 = [1,2,3,4]
#print(geometric_mean(list1, 5))
print(geo_mean([2], 10))
print(geo_mean([1,2], 3))
print(geo_mean([4, 6, 7, 2], 5))

# beta练习2：
# 画方形
def draw_square(size):
    box = ""
    if size == 0:
        return box
    if size == 1:
        return "#"
    if size == 2:
        return "##\n##"
    if size > 2:
        for index in range(3,size+1):
            box += "#" + " " * (size-2) + "#\n"
        box = "#" * size + "\n" + box + "#" * size
    return box

print(draw_square(4))

