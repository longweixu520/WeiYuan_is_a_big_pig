import math
import numpy as np
import matplotlib.pyplot as plt

#待求解数值积分sqrt(x) * log(x)
def f1(x):
    if (float(np.fabs(x))<1e-15) :
        return 0
    y=np.sqrt(x) * np.log(x)
    return y
#待求解数值积分sin(x)/x
def f2(x):
    if (float(np.fabs(x)) < 1e-15):
        return 1
    y=np.sin(x)/x
    return y


#复化辛普森公式 f为待求解积分 a为积分下限 b为积分上限 n为区间等分数
def FHXPs(f,a,b,n):
    si=0.0
    h = (b - a) / (2 * n)
    si=f(a)+f(b)
    for k in range(1,int(n)):
        xk = a + k * 2 * h
        si = si + 2 * f(xk)
    for k in range(int(n)):
        xk = a + (k * 2 + 1) * h
        si = si + 4 * f(xk)
    FHXPs = si*h/3
    print("复化辛普森公式计算结果为：FHXPs = ", FHXPs)


def main():
    a = input("a = ")  
    b = input("b = ")  
    a = float(a)  
    b = float(b)
    n = input("n = ") 
    n = float(n)
    FHXPs(f1,a,b,n) 
    FHXPs(f2,a,b,n) 


if __name__ == '__main__':
    main()
