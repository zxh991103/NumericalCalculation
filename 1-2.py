import numpy as np
import matplotlib.pyplot as plt
N=100


l1=[2]
for i in range(1,N):
    l1.append(15/(2*l1[i-1]+1))

l2=[]
for i in range(N):
    l2.append(i)

x=np.asanyarray(l2)
y=np.asanyarray(l1)

plt.scatter(x, y)
plt.show()