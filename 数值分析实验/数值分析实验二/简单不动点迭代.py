import math
import matplotlib.pyplot as plt

# 显示中文
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False



def f(x):
    return 1.6 + 0.99 * math.cos(x)

# 简单不动点迭代法
def fixed_point_iteration(x0, tolerance=1e-6, max_iter=100):
    x = x0
    iterations = [x] 
    
    for _ in range(max_iter):
        x_new = f(x)
        iterations.append(x_new)
        # 检查是否收敛
        if abs(x_new - x) < tolerance:
            break
        x = x_new
    
    return x, iterations

# 初始值
x0 = math.pi / 2


root, iterations = fixed_point_iteration(x0)

# 输出结果
print(f"收敛的根是: {root}")
print(f"迭代次数: {len(iterations)}")

# 绘制收敛过程图
plt.plot(range(len(iterations)), iterations, marker='o')
plt.xlabel('迭代次数')
plt.ylabel('x值')
plt.title('简单不动点迭代法收敛过程')
plt.grid(True)
plt.show()

# 验证收敛速度
errors = [abs(iterations[i] - iterations[i-1]) for i in range(1, len(iterations))]
plt.plot(range(1, len(errors) + 1), errors, marker='x', color='r')
plt.xlabel('迭代次数')
plt.ylabel('误差')
plt.title('不动点迭代法收敛速度')
plt.grid(True)
plt.show()
