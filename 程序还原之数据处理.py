import random                   # 导入 random 库，用于处理随机相关的功能
import numpy as np              # 导入 numpy 库，用于计算平均数等

a = [i for i in range(1, 11)]   # 列表生成式：生成[1, 11)之间的整数
# 等价于 a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = random.sample(a, k=5)       # random 库中的 sample 函数用来不重复的抽样，参数 k 表示抽样个数
print(b)
c = random.choices(a, k=5)      # random 库中的 choices 函数用来有重复的抽样，k 的含义同上
print(c)

total = np.sum(a)               # 对列表 a 求和
average = np.mean(a)            # 对列表 a 求算术平均数
std = np.std(a)                 # 对列表 a 求标准差
var = np.var(a)                 # 对列表 a 求方差
print(total, average, std, var)