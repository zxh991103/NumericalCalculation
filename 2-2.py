import numpy as np
import math
import scipy as scipy
from scipy import linalg

A = 4 * np.eye(50, 50)
for i in range(49):
    A[i][i + 1] = 1
    A[i + 1][i] = 1
B = 3 * np.ones(50)  # data 1
# B=np.ones(50)           #data 2
# for i in range(1,50,2):
#     B[i]+=1


def cal(A,B,N,K):
    xa = [np.ones(N).tolist()]
    for i in range(K):
        t = []
        tem = (B[0] - xa[i][1]) / A[0][0]
        t.append(tem)
        for j in range(1, N-1):
            tem = (B[j] - (t[j - 1] + xa[i][j + 1])) / A[j][j]
            t.append(tem)
        tem = (B[0] - t[N-2]) / A[N-1][N-1]
        t.append(tem)
        xa.append(t)
    return xa[len(xa)-1]


print(cal(A,B,50,500))