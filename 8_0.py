import numpy as np

A0 = [
    [4, -1, 1],
    [-1, 3, -2],
    [1, -2, 3]
]
A = np.array(A0)




def findmax(x):
    t = np.abs(x).tolist()
    xmax = np.max(t)
    res = 0
    for i in range(len(t)):
        if t[i] == xmax:
            res = i
            break
    return xmax, res


def f1(N=1000000, TOL=1e-18):
    xr=[]
    x = [1, 1, 1]
    X = np.array(x).T
    k = 1
    xmax, p = findmax(X)
    X = X / xmax
    while k < N:
        k += 1
        y = np.matmul(A, X)
        ymax, yp = findmax(y)
        mu = ymax
        xr.append(mu)
        if ymax == 0:
            print(X)
            print('please reselect x')
            break
        err, no = findmax(X - (y.T) / ymax)
        X = y.T / ymax

        if err < TOL:
            xm, xp = findmax(X)
            return mu, X/xm, k,xr
            break


print(f1())


def two(X):
    sum = 0
    for i in X:
        sum += i * i
    sum = pow(sum, 0.5)
    return sum


def f2(N=1000000, TOL=1e-18):
    x = [1, 1, 1]
    xr = []
    X = np.array(x).T
    X = X / two(X)
    k = 1
    while k <= N:
        k += 1
        y = np.matmul(A, X)
        mu = np.matmul(X.T, y)
        xr.append(mu)
        if two(y) == 0:
            print('Eig', X)
            print('reselect')
        ERR = two(X - y / two(y))
        X = y / two(y)
        if ERR < TOL:
            xm,xp=findmax(X)
            return mu, X/xm, k,xr


print(f2())


def cal(A, B):
    x = np.linalg.solve(A, B)
    return x.T


def calq(X):
    q = np.matmul(np.matmul(X.T, A), X) / np.matmul(X.T, X)
    return q


def f3(N=100000, TOL=1e-18):
    x = [1, -0.1, 0.2]
    xr=[]
    X = np.array(x).T
    k = 1
    q = calq(X)
    xr.append(q)
    xmax, xp = findmax(X)
    X = X / xmax

    while k <= N:
        k += 1
        I = np.eye(len(A))
        q = calq(X)
        xr.append(q)
        try:
            y = np.array(cal(A - q * I, X)).T
        except:
            ymax, yp = findmax(y)
            return q, y/ ymax, k,xr
        else:
            ymax, yp = findmax(y)
            mu = ymax
            ERR, no = findmax(X - (y / ymax))
            X = y / ymax

            if ERR < TOL:
                mu = (1 / mu) + q
                xm, xp = findmax(X)
                return mu, X/xm, k,xr


print(f3())
