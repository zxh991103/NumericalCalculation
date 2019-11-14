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


xa = [np.ones(50).tolist()]

for i in range(500):
    t = []
    tem = (B[0] - xa[i][1]) / A[0][0]
    t.append(tem)
    for j in range(1, 49):
        tem = (B[j] - (t[j - 1] + xa[i][j + 1])) / A[j][j]
        t.append(tem)
    tem = (B[0] - t[48]) / A[49][49]
    t.append(tem)
    xa.append(t)

print(xa[len(xa)-1])