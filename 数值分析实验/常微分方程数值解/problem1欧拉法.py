import math
import matplotlib.pyplot as plt

def euler_solver(f, x0, y0, h, xn):
    # f : dy/dx = f(x, y)
    x_values, y_values = [x0], [y0]
    while x_values[-1] < xn:
        x_i, y_i = x_values[-1], y_values[-1]
        y_new = y_i + h * f(x_i, y_i)
        y_values.append(y_new)
        x_values.append(x_i + h)
    return x_values, y_values


def f(x, y):
    return math.sqrt(x**2 + y**2)  # 这是给定的微分方程

# 初始条件和步长设置
x0, y0 = 0, 1
h = 0.1
xn = 1

# 求解欧拉法
x, y = euler_solver(f, x0, y0, h, xn)

# 输出结果
for i in range(len(x)):
    print(f"x = {x[i]:.2f}, y = {y[i]:.4f}")

# 绘制解的曲线
plt.plot(x, y, label="Euler's Method")
plt.title("Solution of dy/dx = sqrt(x^2 + y^2)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
