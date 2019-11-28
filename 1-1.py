import numpy as np
import matplotlib.pyplot as plt
N=4


l1=[2]
for i in range(1,N):
    l1.append(15-pow(l1[i-1],2))

l2=[]
for i in range(N):
    l2.append(i)

x=np.asanyarray(l2)
y=np.asanyarray(l1)

plt.scatter(x, y)
plt.savefig('2-1-1.png')
plt.show()


