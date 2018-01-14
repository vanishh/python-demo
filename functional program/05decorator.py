# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:53:38 2018

@author: Administrator
"""

# 可以使用functools模块
import functools

# 函数也是一个对象
# 函数对象有一个__name__ 属性 可以获取函数名字

# 装饰器
# 在代码运行期间动态增加功能的方式 叫为装饰器
# 本质上 装饰器就是一个返回函数的高阶函数

# 定义装饰器
def log(func):
    # 最后一步
    # 需要将原始函数的__name__属性复制到wrapper()函数中
    @functools.wraps(func)
    def wrapper(*args, **kw):
        # 需要扩展的功能
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper

# 把@log放在now()函数定义处，相当于执行了语句 now = log(now)
# 用装饰器装饰函数now()
@log
def now():
    print("2018-01-14")
    
now()

# 如果装饰器需要传参数

def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log1("test") # 相当于执行log('test')(now)
def time():
    print("2018-01-14")

time()
print(time.__name__)  # 被装饰器装饰过的函数，__name__属性变为wrapper

# 设计一个decorator 用于记录程序的运行时间
def metric(fn):
    @functools.wraps(fn)
    def decorator(*args, **kw):
        print("%s executed in %s ms" % (fn.__name__, 2.3))
        return fn(*args, **kw)
    return decorator

@metric
def add(x, y):
    return x + y
print(add(4, 5))