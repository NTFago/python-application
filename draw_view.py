import matplotlib.pyplot as plt     # 导入matplotlib库中的pyplot模块，用于绘图
import math     # 导入math库用于计算解析式

# 定义解析式
def f(x):
    return math.pow(x, 2)

x = [i for i in range(-5, 6)]   # x的取值范围，即函数f(x)的定义域
y = [f(j) for j in x]           # 定义域内所对应的函数值

# print(x, y)   # 打印测试

plt.plot(x, y, label="$y=x^2$", linestyle="--")
plt.legend(loc='best')  # 自动分配图例到最佳位置
plt.show()
