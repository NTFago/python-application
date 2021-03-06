import matplotlib.pyplot as plt     # 导入matplotlib库中的pyplot模块，用于绘图
import numpy as np                  # 导入numpy库用于计算解析式

# 定义函数解析式
def f(x):   # f(x) = x^2
    return pow(x, 2)

x = np.arange(-5, 5, 0.1)       # x取值的numpy数组
y = np.array([f(i) for i in x]) # y取值的numpy数组