def cal(A, B):
    x = np.linalg.solve(A, B)
    return x


import numpy as np
import math


def ct(n):
    PI = math.pi
    de = PI / 100
    return de * n


x11 = [ct(0), ct(7), ct(20), ct(29), ct(32), ct(50), ct(64), ct(70), ct(82), ct(90), ct(100)]

x21 = [ct(0), ct(4), ct(10), ct(12), ct(14), ct(20), ct(23), ct(27), ct(35), ct(40), ct(43), ct(55), ct(61), ct(65),
       ct(70), ct(83),
       ct(87), ct(91), ct(94), ct(98), ct(100)]


def initial(x0=0.0, xn=math.pi, n=10, x=x11):
    y = []
    for i in range(n + 1):
        y.append(math.sin(x[i]))

    a = np.array(y)

    h = []
    for i in range(n):
        h.append(x[i + 1] - x[i])

    return a, h, y


def createAb(h, a, choice=0, n=10):
    if choice == 0:
        A = np.zeros((n + 1, n + 1))
        A[0][0] = 1
        A[n][n] = 1
        for i in range(1, n):
            A[i][i - 1] = h[i - 1]
            A[i][i] = 2 * (h[i - 1] + h[i])
            A[i][i + 1] = h[i]
        b = np.zeros(n + 1)
        for i in range(1, n):
            b[i] = 3 * (a[i + 1] - a[i]) / h[i] - 3 * (a[i] - a[i - 1]) / h[i - 1]
        return A, b
    if choice == 1:
        A = np.zeros((n + 1, n + 1))
        A[0][0] = 2*h[0]
        A[0][1] = h[0]
        A[n][n-1] = 2*h[n-1]
        A[n][n] = h[n-1]
        for i in range(1, n):
            A[i][i - 1] = h[i - 1]
            A[i][i] = 2 * (h[i - 1] + h[i])
            A[i][i + 1] = h[i]
        b = np.zeros(n + 1)
        for i in range(1, n):
            b[i] = 3 * (a[i + 1] - a[i]) / h[i] - 3 * (a[i] - a[i - 1]) / h[i - 1]
        return A, b
    if choice == 2:
        A = np.zeros((n + 1, n + 1))
        A[0][0] = h[0]*2/3
        A[0][1] = h[0]*2
        A[0][n-1] = h[n-1]*2/3
        A[0][n] = h[n - 1]/ 3
        A[n][0] = 1
        A[n][n-1]=-1
        for i in range(1, n):
            A[i][i - 1] = h[i - 1]
            A[i][i] = 2 * (h[i - 1] + h[i])
            A[i][i + 1] = h[i]
        b = np.zeros(n + 1)
        b[0]=(a[1]-a[0])/h[0] - (a[n]-a[n-1])/h[n-1]
        for i in range(1, n):
            b[i] = 3 * (a[i + 1] - a[i]) / h[i] - 3 * (a[i] - a[i - 1]) / h[i - 1]
        return A, b
    if choice==3:
        A = np.zeros((n + 1, n + 1))
        A[0][0] = 1
        A[0][1] = -1

        A[n][n] = 1
        A[n][n - 1] = -1
        for i in range(1, n):
            A[i][i - 1] = h[i - 1]
            A[i][i] = 2 * (h[i - 1] + h[i])
            A[i][i + 1] = h[i]
        b = np.zeros(n + 1)

        for i in range(1, n):
            b[i] = 3 * (a[i + 1] - a[i]) / h[i] - 3 * (a[i] - a[i - 1]) / h[i - 1]
        return A, b


def calcd(a, c, h, n=10):
    b = np.zeros(n)
    d = np.zeros(n)
    for i in range(n):
        b[i] = (a[i + 1] - a[i]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])
    return b, d


N = 10

a, h, y = initial()

A, B = createAb(h, a, 3, N)

c = cal(A, B)

b, d = calcd(a, c, h, N)

print(len(a))
print(len(b))
print(len(c))
print(len(d))


from matplotlib import pyplot as plt

from scipy import interpolate


def everysection(a,b,c,d,x,i):
    xt = np.linspace(x[i], x[i+1], 100)
    y = d[i] * (xt-x[i]) ** 3 + c[i] * (xt-x[i]) ** 2 + b[i] *(xt-x[i])+a[i]
    plt.plot(xt, y, color="green", linewidth=0.5)

def inplot():
    x = np.linspace(0, np.pi, 100, endpoint=True)
    y = np.sin(x)
    # plt.plot(x, y,color='pink',linewidth=3)
def pAll(a,b,c,d,x,N):
    for i in range(N):
        everysection(a,b,c,d,x,i)
    plt.scatter(x,a,color='red',marker='o')
    plt.savefig('a.png')
    plt.show()

inplot()
pAll(a,b,c,d,x11,N)


