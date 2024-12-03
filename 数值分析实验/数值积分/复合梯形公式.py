import numpy as np
import math
import matplotlib.pyplot as plt

# 待求解数值积分sqrt(x) * log(x)
def f1(x):
    if (float(np.fabs(x))<1e-15) :
        return 0
    y=np.sqrt(x) * np.log(x)
    return y
# 待求解数值积分sin(x)/x
def f2(x):
    if (float(np.fabs(x)) < 1e-15):
        return 1
    y=np.sin(x)/x
    return y


#复化梯形公式 f为待求解积分 a为积分下限 b为积分上限 n为区间等分数
def FHTx(f,a,b,n):
    ti=0.0
    h=(b-a)/n
    ti=f(a)+f(b)
    for k in range(1,int(n)):
        xk=a+k*h
        ti = ti + 2 * f(xk)
    FHTx = ti*h/2
    print("复化梯形公式计算结果为：FHTx = ", FHTx)

def main():
    a = input("a = ")  
    b = input("b = ")  
    a = float(a)  
    b = float(b)
    n = input("n = ") 
    n = float(n)

    FHTx(f1,a,b,n)
    FHTx(f2,a,b,n) 

if __name__ == '__main__':
    main()
