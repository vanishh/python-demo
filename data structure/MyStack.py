# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 00:19:24 2018

@author: Administrator
"""
# 定义栈类和栈中的节点
# 栈有长度属性、当前栈顶元素、
# 栈有入栈方法、弹栈方法、获取栈顶元素方法
class MyStack(object):
    def __init__(self):
        # 前驱
        self.before = None
        # 后继
        self.behind = None
        # 栈长度
        self.__length = 0
        # 栈顶位置
        self.__top = -1
        # 栈存储空间
        self.list = []
            
    def get_length(self):
        return self.__length;
    def get_top(self):
        return self.__top
    
    # 获取栈顶元素
    def top(self):
        if self.__length <= 0:
            return None
        else:
            return self.list[self.__top]
            
    # 入栈操作
    # 元素加入空间头部，length 加1， top位置加1
    def push(self, node):
        if not isinstance(node, Node):
            return
        if node == None:
            return
        else:
            self.list.append(node)
            self.__length += 1
            self.__top += 1

    # 出栈操作
    # 空间头部元素弹出，长度减1，top-1
    def pop(self):
        if self.isEmpty() == False:
            self.__length -= 1
            self.__top -= 1
            return self.list.pop()
        return None
    # 栈是否为空
    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False
    
    # 获取站内所有元素
    def print_list(self):
        for index in self.list:
            if isinstance(index, Node):
                print(index.get_value())
 # 创建节点
# 节点有值属性
class Node(object):
    def __init__(self, value):
        self.value = value
    
    def set_value(self, value):
        self.value = value
    def get_value(self):
        return self.value


my_stack = MyStack()
print("init:", my_stack.get_top())
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
# 添加元素
my_stack.push(node1)
my_stack.push(node2)
my_stack.push(node3)
my_stack.print_list()
print("top:", my_stack.get_top())
result = my_stack.top()
print("top element:", result.get_value())
print("-" * 20)
# 出栈
result = my_stack.pop()
my_stack.print_list()
print("-" * 20)
# 在入栈
node4 = Node(40)
my_stack.push(node4)
my_stack.print_list()