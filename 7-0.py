import numpy as np

x_array = np.array([-2, -1, 0, 1, 2])
y_array = np.array([0,1,2,1,0])
n = 2
m = len(x_array)  # 方程个数

A = np.ones(m).reshape((m, 1))
for i in range(n):
    A = np.hstack([A, (x_array ** (i + 1)).reshape((m, 1))])

from numpy.linalg import solve
alpha=np.dot(A.T, A)
belta= np.dot(A.T, y_array.T)
X = solve(alpha,belta)
print(X)
print(alpha)
print(belta)
#https://wenku.baidu.com/view/886e944ffe00bed5b9f3f90f76c66137ef064f5a.html p8
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100, endpoint=True)
y = X[2]*x*x+X[1]*x+X[0]
plt.plot(x, y,color='pink',linewidth=1)
plt.scatter(x_array,y_array)
plt.savefig('8.png')
plt.show()

