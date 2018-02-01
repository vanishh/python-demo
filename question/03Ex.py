# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 计算m ~ n之间整数的和
def sum(m, n):
    sumRange = 0
    if m > n:
        return
    else:
        for index in range(m, n+1):
            sumRange += index
        return sumRange
sum(5, 8)

# 2018年1月28日练习题
#题目1：使用Python编程，求1～100间所有偶数的和。
sum = 0
for index in range(1, 101):
    if index % 2 == 0:
       sum += index
       
       
print(sum)

#题目2：用Python编写程序，输入一年份，判断该年份是否是闰年并输出结果。  
#       注：凡符合下面两个条件之一的年份是闰年。 
#  （1） 能被4整除但不能被100整除。 
#  （2） 能被400整除。
while True:
    year = int(input("输入年份:"))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("%d是闰年！" % year)
    else:
        print("%d不是闰年！" % year)
        
#题目3：用Python编程，假设一年期定期利率为3.25%，计算一下需要过多少年，
#一万元的一年定期存款连本带息能翻番？
year = 1
while True:
    if 10000 * (1 + 0.0325) ** year >= 20000:
        print("10000元存%d年能翻一倍" % year)
        break
    else:
        year += 1

#题目4：猜数游戏。预设一个0~9之间的整数，
#让用户猜一猜并输入所猜的数，如果大于预设的数，
#显示“太大”；小于预设的数，显示“太小”，如此循环，直至猜中该数，显示“恭喜！你猜中了！”。

number = 8
while True:
    inputNumber = int(input("请输入一个数："))
    if inputNumber > number :
        print("太大")
    elif inputNumber < number:
        print("太小")
    else:
        print("恭喜你，猜中了！")
        break
    
# 题目5：输入一个时间（小时:分钟:秒），输出该时间经过5分30秒后的时间。
time = input("请输入一个时间（格式：hh:mm:ss）:")
list1 = list(time.split(":"))
hour = int(list1[0])
minute = int(list1[1])
second = int(list1[2])

if second >= 30:
    if minute >= 54:
        if hour == 23:
            hour = 0
        else:
            hour += 1
        minute = minute + 6 - 60
    else:
        minute += 6
    second = second + 30 - 60
else:
    if minute >= 55:
        if hour == 23:
            hour = 0
        else:
            hour += 1
        minute = minute + 5
    else:
        minute += 5
    second += 30
        
print("%d:%d:%d" % (hour, minute, second))
        

# 题目6：从键盘接收若干个整数,进行排序（从小到大或者从大到小），并将排序结果在屏幕上输出。
# 12 23 25 16 7 23 34
# 这不是冒泡，这是什么排序？？
list1 = [12, 23, 25, 16, 7, 23, 34]

for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1)

#题目7：输入一个数，判断这个数是否为素数，并输出判断结果。
# （所谓素数，是指除了1和该数本身之外，不能被其它任何整数整除的数。)
while True:
    number1 = int(input("请输入一个数："))
    flag = True
    for index in range(2, number1):
        if number1 % index == 0:
            print("%d不是素数" % number1)
            flag = False
            break
        else:
            continue
        
    if flag == True:
        print("%d是素数" % number1)
        break

# 题目8：一个数如果恰好等于它的因子之和，这个数就称为“完数”。
# 例如，6的因子为1、2、3，而6=1+2+3，因此6是完数。
# 编程，找出1000之内的所有完数，并输出该完数及对应的因子。

factor = []
result = {}
for index in range(1, 1001):
    for i in range(1, index):
        if index % i == 0:
            factor.append(i)
 
    if sum(factor) == index:
#        print("%d为完数" % index)
#        print("因子为：", factor)
        result[str(index)] = factor
    factor.clear()
    
for key, value in result.items():
    print("%s:%s" % (key, value))