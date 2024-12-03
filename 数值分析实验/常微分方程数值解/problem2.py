import matplotlib.pyplot as plt
import math

# 定义常微分方程的右侧函数
def f(x, y, alpha):
    return alpha * y - alpha * x + 1

# 四阶龙格库塔法实现
def runge_kutta(alpha, h, x0, y0, x_end):
    # 初始化 x 和 y 的列表
    x_vals = [x0]
    y_vals = [y0]
    
    x = x0
    y = y0
    
    # 进行迭代计算
    while x < x_end:
        k1 = h * f(x, y, alpha)
        k2 = h * f(x + h/2, y + k1/2, alpha)
        k3 = h * f(x + h/2, y + k2/2, alpha)
        k4 = h * f(x + h, y + k3, alpha)
        
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
        
        x_vals.append(x)
        y_vals.append(y)
    
    return x_vals, y_vals

# 准确解函数
def exact_solution(x, alpha):
    return math.exp(alpha * x) + x

# 设置初值
x0 = 0
y0 = 1
x_end = 1
h = 0.01

# 定义不同的 alpha 值
alpha_values = [40, 0.1, -0.1, -40]

# 绘制计算结果
plt.figure(figsize=(10, 6))

for alpha in alpha_values:
    # 使用龙格库塔方法求解
    x_vals, y_vals = runge_kutta(alpha, h, x0, y0, x_end)
    
    # 计算准确解
    exact_vals = [exact_solution(x, alpha) for x in x_vals]
    
    # 绘制图形
    plt.plot(x_vals, y_vals, label=f'RK4, α = {alpha}')
    plt.plot(x_vals, exact_vals, '--', label=f'Exact Solution, α = {alpha}')

# 图表设置
plt.title('Comparison of RK4 and Exact Solution for Different α values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
