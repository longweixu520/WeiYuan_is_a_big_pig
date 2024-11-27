import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False


def func(x):
    return 1 / (1 + x ** 2)


def Newton(l, r):
    global xList, bList
    if l == r:
        return func(xList[l])
    left = Newton(l, r - 1)
    right = Newton(l + 1, r)
    numb = (left - right) / (xList[l] - xList[r])
    if l == 0:
        bList[r] = numb
    return numb


def Newton_function(n, x):
    global bList
    yList = list(np.ones(n))
    for i in range(n - 1):
        temp = 1
        j = i
        while j > -1:
            temp *= (x - xList[j])
            j -= 1
        yList[i + 1] = temp
    numb = 0
    for i in range(n):
        numb = numb + bList[i] * yList[i]
    return numb


def main():
    global xList, bList
    xList = list()
    bList = list(np.zeros(100))

    n = int(input('请输入点的个数（至少为16）：\n'))

    # 生成n个等距节点
    xList = np.linspace(-5, 5, n)

    bList[0] = func(xList[0])
    Newton(0, len(xList) - 1)

    line = np.arange(-5, 5, 0.1)

    plt.figure(figsize=(8, 18))

    plt.subplot(3, 1, 1)
    plt.title("原函数和选取的点")
    plt.plot(line, func(line), color='g', label='原函数')
    plt.scatter(np.array(xList), func(np.array(xList)), color='r')
    plt.legend(['原函数'])
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.title("牛顿插值法拟合曲线")
    plt.grid()
    plt.plot(line, Newton_function(n, line), color='b', label='拟合函数')
    plt.scatter(np.array(xList), func(np.array(xList)), color='r')
    plt.legend(['拟合函数'])

    plt.subplot(3, 1, 3)
    plt.title("原函数和拟合函数的重合度")
    plt.grid()
    plt.plot(line, func(line), color='g', label='原函数')
    plt.scatter(np.array(xList), func(np.array(xList)), color='r')
    plt.plot(line, Newton_function(n, line), color='b', label='拟合函数')
    plt.legend(['原函数', '拟合函数'])

    plt.show()


if __name__ == "__main__":
    main()
