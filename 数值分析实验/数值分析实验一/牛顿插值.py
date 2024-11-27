import numpy as np
from matplotlib import pyplot as plt


def newton_interpolation(x, x_list, y_list):
    n = len(x_list)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_list

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = (diff_table[i + 1, j - 1] - diff_table[i, j - 1]) / (x_list[i + j] - x_list[i])

    result = diff_table[0, 0]
    product_term = 1
    for i in range(1, n):
        product_term *= (x - x_list[i - 1])
        result += product_term * diff_table[0, i]

    return result


# 主函数
x_list = [0, 1, 4, 9, 16, 25, 36, 49, 64]
y_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

x_vals = np.linspace(min(x_list), max(x_list), 500)
y_vals = newton_interpolation(x_vals, x_list, y_list)

plt.plot(x_vals, y_vals,color='green')
plt.scatter(x_list, y_list, color='red')

plt.show()