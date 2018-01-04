# print 测试
print(100 + 200 + 300)
print("test", "geyang", "nihao")
print("1024 * 768 = %d" % (1024 * 768))
print("hello %s" % 'world!')
print("中文测试");
# 输入内容
name = input("please input your name!")
print("my name is %s" % name)
print("my name is " + name);

# 计算小明成绩提升多少
print("计算小明成绩提升")
before = float(input("小明之前的成绩:"))
after = float(input("小明之后的成绩:"))
rate = (after - before) / before * 100
print("小明之前的成绩%f, 之后的成绩%f, 提升了%d %%" % (before, after, rate));

