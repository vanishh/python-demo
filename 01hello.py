# print 测试
print(100 + 200 + 300)
print("test", "geyang", "nihao")
print("1024 * 768 = %d" % (1024 * 768))
print("hello %s" % 'world!')
print("中文测试");

# 输入内容
# input 获取的数据 都是以字符串方式保存的；
# 即使输入的是数据，那么也是以字符串方式保存
name = input("please input your name!")
print("my name is %s" % name)
print("my name is " + name);

# 计算小明成绩提升多少
print("计算小明成绩提升")
before = float(input("小明之前的成绩:"))
after = float(input("小明之后的成绩:"))
rate = (after - before) / before * 100
print("小明之前的成绩%f, 之后的成绩%f, 提升了%d %%" % (before, after, rate));


# 字符串 字符的组合
str1 = str("nihao test")
print(str1[0])

# 字符串常用函数
print(str1.find("test"))
# 如果没有找到字符串 提示错误 ValueError: substring not found
print(str1.index("test")) 
# replace 将指定的参数1 替换为参数2
print(str1.replace("test", " geyang"))

# split(分割表达式) 分割字符串
print(str1.split(" "))
print(str1.startswith("ni"))
print(str1.endswith("ni"))

# strip() 去除字符串左右两边的空格
str2 = "   nihao     "
print(str2.strip())

# 大小写转换
print(str2.strip().upper())
print(str2.strip().capitalize())

# 练习 输入字符串 将小写字母转换为大写
listTemp = list(input("请输入字符串:"))
listNew = list()
for element in listTemp:
    if element >= 'a' and element <= 'z':
        upperElement = element.upper()
        listNew.append(upperElement)
    else:
        listNew.append(str(element))

print(listNew)
        
# 练习2 随机输入8位以内的正整数 要求：1求它是几位数 2逆序打印各位数
number1 = int(input("请输入数字:"))
n = 10
count = 1
while(n):
    result = number1 / n
    if(result > 1):
        count = count + 1
        n = n * 10
    else:
        break
print(count)


# 练习3 输入一行字符 统计出其中的各个分类
lineTempList = list(input())
countSmall = 0
countLarge = 0
countSpace = 0
countOther = 0
for char in lineTempList:
    if char >= 'a' and char <= 'z':
        countSmall += 1
    elif char >= 'A' and char <= 'Z':
        countLarge += 1
    elif char == ' ':
        countSpace += 1
    else:
        countOther += 1
print("small:", countSmall)
print("large:", countLarge)
print("space:", countSpace)
print("other:", countOther)
        
    
    