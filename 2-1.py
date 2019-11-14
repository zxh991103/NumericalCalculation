import numpy as np
import math
import scipy as scipy
from scipy import linalg

x = [[4, -1, 1],
     [4, -8, 1],
     [-2, 1, 5]]

y = [7, -21, 15]

# LU分解
X = np.array(x)
Y = np.array(y)
n = 3

l, u = scipy.linalg.lu(X, True)

y0 = [0, 0, 0]
sum = 0
for i in range(n):
    t = 0
    for j in range(sum):
        t += y0[j] * l[i][j]
    y0[i] = (Y[i] - t) / l[i][sum]
    sum += 1

y1 = [0, 0, 0]
sum = 0
for i in range(n):
    t = 0
    for j in range(sum):
        t += y1[n - j - 1] * u[n - i - 1][n - j - 1]
    y1[n - i - 1] = (y0[n - i - 1] - t) / u[n - i - 1][n - sum - 1]
    sum += 1

print(y1)


#Jacobi
x = [[4, -1, 1],
     [4, -8, 1],
     [-2, 1, 5]]

y = [7, -21, 15]

X = np.array(x)
Y = np.array(y)
n = 3

xa=[[1,1,1]]
for i in range(1000):
    if xa[i]==[2,4,3]:
        break;
    tem=[]
    for j in range(n):
        t=0
        for k in range(n):
            if k!=j:
                t+=X[j][k]*xa[i][k]
        tem.append((Y[j]-t)/X[j][j])
    xa.append(tem)

print(xa[len(xa)-1])

#Gauss-Seidel
x = [[4, -1, 1],
     [4, -8, 1],
     [-2, 1, 5]]

y = [7, -21, 15]

X = np.array(x)
Y = np.array(y)
n = 3


xa=[[1,1,1]]
for i in range(1000):
    if xa[i]==[2,4,3]:
        break;
    tem=[]
    for j in range(n):
        t=0
        for k in range(len(tem)):
            if k!=j:
                t+=X[j][k]*tem[k]
        for k in range(len(tem),n):
            if k!=j:
                t+=X[j][k]*xa[i][k]

        tem.append((Y[j]-t)/X[j][j])
    xa.append(tem)

print(xa[len(xa)-1])


