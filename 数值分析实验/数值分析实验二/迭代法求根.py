import math


def f(x):
    return x**3 + 3*x**2 - 1

def f_prime(x):
    return 3*x**2 + 6*x

# 牛顿法迭代函数
def newton_method(x0, tol=0.5e-8, max_iter=1000):
    x = x0
    iter_count = 0
    
    while iter_count < max_iter:
        fx = f(x)
        fx_prime = f_prime(x)
        
        if fx_prime == 0:
            print("导数为零，无法继续迭代。")
            return None
        
        # 迭代更新x的值
        x_new = x - fx / fx_prime
        
        # 检查误差是否小于指定的容忍度
        if abs(x_new - x) < tol:
            return x_new
        
        x = x_new
        iter_count += 1
    
    print("迭代次数超过最大值")
    return None

# 初始猜测值
x0 = -0.7  

# 求解根
root = newton_method(x0)
if root is not None:
    print(f"方程的根为: {root}")
