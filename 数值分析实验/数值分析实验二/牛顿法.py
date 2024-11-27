import math

# 定义方程及其导数
def f(x):
    return x**9 - 522 + math.exp(x)

def f_prime(x):
    return 9*x**8 + math.exp(x)

# 牛顿法迭代函数
def newton_method(x0, tol=1e-8, max_iter=1000):
    x = x0
    iter_count = 0
    errors = []  
    while iter_count < max_iter:
        fx = f(x)
        fx_prime = f_prime(x)
        
        if fx_prime == 0:
            print("导数为零，无法继续迭代。")
            return None, errors
        
        # 迭代更新x的值
        x_new = x - fx / fx_prime
        
        # 记录当前误差
        errors.append(abs(x_new - x))
        
        # 检查误差是否小于指定的容忍度
        if abs(x_new - x) < tol:
            return x_new, errors
        
        x = x_new
        iter_count += 1
    
    print("迭代次数超过最大值")
    return None, errors


x0 = 1.9  


root, errors = newton_method(x0)

if root is not None:
    print(f"方程的根为: {root}")
    
    print("每次迭代的误差:")
    for i, error in enumerate(errors):
        print(f"迭代 {i+1}: 误差 = {error}")
    
    
    if len(errors) > 2:
        print("\n验证收敛速度（误差比值）:")
        for i in range(2, len(errors)):
            ratio = errors[i] / errors[i-1]  
            print(f"误差比值 (迭代 {i}): {ratio}")
