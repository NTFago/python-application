import matplotlib.pyplot as plt # 绘图
import numpy as np              # 科学计算
import math                     # 解析式定义
"""
-------math库常用函数-------
math.e   自然常数e
math.pi  圆周率pi
math.degrees(x)	 弧度转度
math.radians(x)	 度转弧度
math.log(x[, base])	 返回x的以base为底的对数，base默认为e
math.log10(x)	 返回x的以10为底的对数
math.pow(x, y)	 返回x的y次方
math.sqrt(x)	 返回x的平方根
math.sin(x)	 返回x（弧度）的三角正弦值（cos,tan,asin,acos,atan亦如此）
"""

# 自行定义函数部分, 也可以用numpy库来定义
def f(x):
    func = math.log(x) + 2 * x - 6   # 函数解析式
    return func


# 控制台获取输入
ε = float(input("请输入精度值："))
a = float(input("请输入区间[a, b]中a的值："))
b = float(input("请输入区间[a, b]中b的值："))

# 循环主体
while math.fabs(a - b) >= ε:    # 为了程序的精度相匹配，使用math库中的fabs方法进行绝对值运算
    c = (a + b) / 2
    if f(a) * f(c) < 0:
        b = c
    elif f(c) == 0:
        a = c
        break
    else:
        a = c

print("函数的零点为：{}".format(a))

# --------------绘图部分----------------
x = np.linspace(a, b*3, int(a*b*5))  # 线性生成值
y = np.log10(x) + 2 * x - 6    # 解析式

plt.figure(figsize=(10, 6))  # 设置图象宽高
plt.plot(x, y, label='函数图像', color='red', linewidth=1)  # 绘图
plt.xlabel('x')  # 标记x
plt.ylabel('y')  # 标记y
# 定义y轴长度
plt.vlines(x=0, ymin=-10, ymax=10, colors="k", linestyles="solid")
# 定义x轴长度
plt.hlines(y=0, xmin=-1, xmax=10, colors="k", linestyles="solid")

plt.rcParams['font.sans-serif'] = ["SimHei"]  # 定义字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 用正常来显示负号
plt.title('f(x)的图象')  # 设置标题
plt.legend(loc='best')  # 自动分配图例到最佳位置
plt.show()  # 显示图象
