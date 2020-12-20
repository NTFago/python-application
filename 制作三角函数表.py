import math     # 导入math库进行运算
import time     # 导入time库进行时间计算

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

s0 = math.sin(math.radians(1 / 60))     # 计算并返回1'的正弦值
c0 = math.sqrt(1 - math.pow(s0, 2))   # 计算并返回1'的余弦值
# 上面一行也可写成 c0 = math.sqrt((1 - s0 ** 2))
print(f"sin1' 的值为：{s0}, cos1' 的值为：{c0}")

s = s0
c = c0
n = 2
degrees = 0     # 储存角度值
minute = 2      # 储存分度值
out_list = []   # 储存输出结果

# 定义函数用于计算正弦值
def calculation(x, y):  # x代表程序中的s， y代表程序中的c
    global s0, c0
    s1 = x*c0 + y*s0
    c1 = math.sqrt(1 - math.pow(s1, 2))
    return s1, c1
    
start = time.time()     # 正式开始运算前的时间戳
# 计算过程
while n <= 5400:
    s, c = calculation(s, c)
    # 优化打印
    if (degrees == 0) and (minute < 60):
        out_put = f"sin{minute}'\t的值为：\t{s}"
        print(out_put)
    else:
        if minute == 60:
            degrees += 1
            minute = 0
        out_put = f"sin{degrees}°{minute}'\t的值为：\t{s}"
        print(out_put)
    out_put = out_put + "\n"
    out_list.append(out_put)
    minute += 1
    n += 1

with open("三角函数表.txt", "w", encoding="utf-8") as f:    # 写出输出结果
    f.writelines(out_list)

end = time.time()       # 运算结束后的时间戳
print(f"计算耗时为{end - start}秒")
