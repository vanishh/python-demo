# -*- coding: utf-8 -*-
"""
Created on Fri May 18 09:17:10 2018

@author: Administrator
"""
# 调用房价数据集，然后使用线性回归的方法对其进行预测
# 打开波士顿房价数据集
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
loaded_data = datasets.load_boston()

# 导入数据
data_x = loaded_data.data
data_y = loaded_data.target

# 设置线性回归模型
model = LinearRegression()
# 训练数据，得出参数
model.fit(data_x, data_y)

# 利用模型，对新数据进行预测，与原标签进行比较
print(model.predict(data_x[:4,:]))
print(data_y[:4])

