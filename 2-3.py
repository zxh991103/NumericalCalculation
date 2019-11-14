import numpy as np


x=12*np.eye(50,50)
for i in range(49):
    x[i+1][i]=-2
    x[i][i+1]=-2
for i in range(48):
    x[i+2][i]=1
    x[i][i+2]=1



y =5*np.ones(50)

X = np.array(x)
Y = np.array(y)
n = 50


xa=[np.ones(50).tolist()]
for i in range(1000):

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