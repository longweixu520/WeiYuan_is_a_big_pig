import math
import matplotlib.pyplot as plt

def newton(g, dg_dy, y0, tol=1e-6, max_iter=100):
    # 使用牛顿法求解方程 g(y) = 0，返回 y 的解
    y = y0
    for _ in range(max_iter):
        g_val = g(y)
        dg_val = dg_dy(y)
        if abs(g_val) < tol:
            return y
        y = y - g_val / dg_val
    raise ValueError("Newton's method did not converge.")

def implicit_euler_solver(f, f_y, x0, y0, h, xn):
    # f : dy/dx = f(x, y)
    # f_y : partial derivative of f with respect to y
    x_values, y_values = [x0], [y0]
    while x_values[-1] < xn:
        x_i, y_i = x_values[-1], y_values[-1]
        
        # 定义隐式方程 g(y) = 0
        def g(y): 
            return y - y_i - h * f(x_i+h, y)
        
        # 定义隐式方程的导数 dg/dy
        def dg_dy(y): 
            return 1 - h * f_y(x_i+h, y)
        
        # 使用牛顿法求解隐式方程
        y_new = newton(g, dg_dy, y_i)
        
        # 更新 x 和 y 值
        x_new = x_i + h
        y_values.append(y_new)
        x_values.append(x_new)
    return x_values, y_values


def f(x, y):
    # 给定的微分方程
    return math.sqrt(x**2 + y**2)

def f_y(x, y):
    # 给定微分方程对 y 的偏导数
    return x / math.sqrt(x**2 + y**2)

# 初始条件和步长设置
x0, y0 = 0, 1
h = 0.1
xn = 1

# 求解隐式欧拉法
x, y = implicit_euler_solver(f, f_y, x0, y0, h, xn)

# 输出结果
for i in range(len(x)):
    print(f"x = {x[i]:.2f}, y = {y[i]:.4f}")

# 绘制解的曲线
plt.plot(x, y, label="Implicit Euler")
plt.title("Solution of dy/dx = sqrt(x^2 + y^2) using Implicit Euler")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
