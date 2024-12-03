import math
import matplotlib.pyplot as plt

def runge_kutta_solver(f, x0, y0, h, xn):
    # f : dy/dx = f(x, y)
    x_values, y_values = [x0], [y0]
    while x_values[-1] < xn:
        x_i, y_i = x_values[-1], y_values[-1]
        k1 = h * f(x_i, y_i)
        k2 = h * f(x_i + h / 2, y_i + k1 / 2)
        k3 = h * f(x_i + h / 2, y_i + k2 / 2)
        k4 = h * f(x_i + h, y_i + k3)
        y_new = y_i + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        y_values.append(y_new)
        x_values.append(x_i + h)
    return x_values, y_values

def f(x, y):
    return math.sqrt(x**2 + y**2)  # 给定的微分方程

# 初始条件和步长设置
x0, y0 = 0, 1
h = 0.1
xn = 1

# 求解四阶 Runge-Kutta 方法
x, y = runge_kutta_solver(f, x0, y0, h, xn)

# 输出结果
for i in range(len(x)):
    print(f"x = {x[i]:.2f}, y = {y[i]:.4f}")

# 绘制解的曲线
plt.plot(x, y, label="4th Order Runge-Kutta")
plt.title("Solution of dy/dx = sqrt(x^2 + y^2) using Runge-Kutta")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
