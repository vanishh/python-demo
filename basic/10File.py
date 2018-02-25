# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:12:52 2018

@author: Administrator
"""

try:
    # r 为打开模式，为read
    f = open("E:\workspace_python\README.md", 'r')
    # read() 可以一次读取文件的全部内容，返回值为str
    result = f.read()
    print(result)
except FileNotFoundError:
    print("没有这个文件！")
finally:
    if f:
        # 由于文件读写时可能产生IOError，使用try finally保证文件一定关闭
        # 文件使用完后必须关闭
        f.close()
        
# 打开文件方式2：with open
# 和前面的try... finally 一样，但是代码更简洁，不用调f.close()
# python会在合适的时候自动将其关闭
with open("E:\workspace_python\README.md", 'r') as f:
    count = 1
    # 按照行的方式把文件内容一次性读取，返回一个列表
    for line in f.readlines():
        print("%d:%s" % (count, line))
        count += 1
        
        
# 写文件
# 模式为w
with open("E:\workspace_python\test.txt", 'w') as f:
    # write() 没有返回值，如果要换行，需要自己添加\n
    f.write("geyang\n")
    
#操作文件和目录
import os
print(os.name)
print(os.environ)

# 操作文件和目录的函数，一部分放在OS模块中，一部分放在os.path中
print(os.path.abspath("."))
os.mkdir("创建目录位置")