import numpy as np
import matplotlib.pyplot as plt
import math

N = 10


def f(t, w):
    return 1 + w * w


def pt(res, color):
    plt.scatter(np.array(res).T[0], np.array(res).T[1], color=color)


def inplot():
    x = np.linspace(0, np.pi / 2.2, 100, endpoint=True)
    y = np.tan(x)
    plt.plot(x, y, color='pink', linewidth=3)


def Euler(a=0, b=math.pi / 2.2, n=N, alpha=0):
    h = (b - a) / n
    t = a
    w = alpha
    res = [[t, w]]
    for i in range(1, n):
        w += h * f(t, w)
        t += h
        res.append([t, w])

    return res


def improvedEuler(a=0, b=math.pi / 2.2, n=N, alpha=0):
    h = (b - a) / n
    t = a
    w = alpha
    res = [[t, w]]
    for i in range(1, n):
        t1 = w + h * f(t, w)
        w += h / 2 * (f(t, w) + f(t + h, t1))
        t += h
        res.append([t, w])
    return res


def RungeKutta(a=0, b=math.pi / 2.2, n=N, alpha=0):
    h = (b - a) / n
    t = a
    w = alpha
    res = [[t, w]]
    for i in range(1, n):
        k1 = h * f(t, w)
        k2 = h * f(t + h / 2, w + k1 / 2)
        k3 = h * f(t + h / 2, w + k2 / 2)
        k4 = h * f(t + h / 2, w + k3)
        w += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
        res.append([t, w])
    return res


res1 = Euler()
pt(res1, 'green')

res2 = improvedEuler()
pt(res2, 'red')

res3 = RungeKutta()
pt(res3, 'blue')

inplot()

plt.show()
