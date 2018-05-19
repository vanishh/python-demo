# -*- coding: utf-8 -*-
"""
Created on Sat May 19 15:39:56 2018

@author: Administrator
"""
# 将包导入到脚本中
import numpy as np
# pyplot() 是matplotlib库中最重要的函数
from matplotlib import pyplot as plt

x = np.arange(1,11)
y = 2 * x + 5

plt.title("matplotlib demo")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x,y, "xb") # 函数绘制
plt.show()    # 图像显示

# 生成正弦波
# 将包导入到脚本中
import numpy as np
# pyplot() 是matplotlib库中最重要的函数
from matplotlib import pyplot as plt
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sinx")
plt.plot(x,y)
plt.show()

# subplot 在一图中显示两部分
import numpy as np 
import matplotlib.pyplot as plt 
# 计算正弦和余弦曲线上的点的 x 和 y 坐标 
x = np.arange(0,  3  * np.pi,  0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
# 建立 subplot 网格，高为 2，宽为 1  
# 激活第一个 subplot
plt.subplot(2,  1,  1)  
# 绘制第一个图像 
plt.plot(x, y_sin) 
plt.title('Sine')  
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2,  1,  2) 
plt.plot(x, y_cos) 
plt.title('Cosine')  
# 展示图像
plt.show()

# plt.bar() 显示柱状图
from matplotlib import pyplot as plt 
x =  [5,8,10] 
y =  [12,16,6] 
x2 =  [6,9,11] 
y2 =  [6,15,7] 
plt.bar(x, y, align =  'center') 
plt.bar(x2, y2, color =  'g', align =  'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis') 
plt.show()

# 小结
# 1.引入matplotlib包 from matplotlib import pyplot as plt
# 2. plt.plot(x,y) 绘制曲线图
# 3. plt.bar(x,y) 绘制柱状图
# 4. plt.title("xx")
# 5. plt.xlabel("x axis")
# 6. plt.show() 图像显示