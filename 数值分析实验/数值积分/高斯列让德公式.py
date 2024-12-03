import numpy as np

# 计算高斯-勒让德积分的节点和权重
def gauss_legendre(n):
    # 计算 n 阶勒让德多项式的根和权重
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

# 高斯-勒让德积分公式
def gauss_legendre_integral(f, a, b, n):
    # 获取节点和权重
    x, w = gauss_legendre(n)
    
    # 计算区间变换
    mid = 0.5 * (b + a)
    half_len = 0.5 * (b - a)
    
    # 计算积分
    integral = 0.0
    for i in range(n):
        # 变换节点
        xi = mid + half_len * x[i]
        integral += w[i] * f(xi)
    
    # 乘以区间长度的一半
    integral *= half_len
    return integral

# 被积函数 1: sqrt(x) * log(x)
def f1(x):
    if (float(np.fabs(x)) < 1e-15):
        return 0
    return np.sqrt(x) * np.log(x)

# 被积函数 2: sin(x)/x
def f2(x):
    if (float(np.fabs(x)) < 1e-15):
        return 1
    return np.sin(x) / x

def main():
    a = input("a = ")  
    b = input("b = ")  
    a = float(a)  
    b = float(b)
    n = input("n = ")  
    n = int(n)  
    
    
    result_f1 = gauss_legendre_integral(f1, a, b, n)
    result_f2 = gauss_legendre_integral(f2, a, b, n)
    
    
    print(f"高斯-勒让德公式计算结果:")
    print(f"∫({a} to {b}) sqrt(x) * log(x) dx = {result_f1}")
    print(f"∫({a} to {b}) sin(x)/x dx = {result_f2}")

if __name__ == '__main__':
    main()
