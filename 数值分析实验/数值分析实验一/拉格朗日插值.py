import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, x_list, y_list):
    n = len(x_list)
    result = 0  # 插值结果初始化为0
    for i in range(n):
        term = y_list[i]  # 当前的 f(x_i) 值
        for j in range(n):
            if i != j:
                term *= (x - x_list[j]) / (x_list[i] - x_list[j])
        result += term  # 累加每项的结果
    return result

# 主函数
x_list = [0, 1, 4, 9, 16, 25, 36, 49, 64]
y_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

x_target = np.linspace(min(x_list), max(x_list), 500)
y_target = [lagrange_interpolation(x, x_list, y_list) for x in x_target]

plt.plot(x_target, y_target,color='blue')
plt.scatter(x_list, y_list, color='red')

plt.show()

