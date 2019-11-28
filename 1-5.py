import math
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
def f(x):
    return 0.5+0.25*pow(x,2)-x*math.sin(x)-0.5*math.cos(2*x)

delta = 0.01

def f_1(x):
    return (f(x+delta)-f(x))/delta

def f_2(x):
    return (f_1(x+delta)-f_1(x))/delta


def g(x):
    return x-f(x)/f_1(x)





def cal(x0):
    res=[0,x0]
    t1=0
    t2=x0
    while ( abs( t1-t2 ) > pow(10,-5) ):
        t1=t2
        t2=g(res[len(res)-1])
        res.append(t2)
    return res


x0=math.pi/2
x1=math.pi*5
x2=math.pi*10

r0=cal(x0)
r1=cal(x1)
r2=cal(x2)

y0=[]
y1=[]
y2=[]

for i in range(len(r0)):
    y0.append(i)

for i in range(len(r1)):
    y1.append(i)

for i in range(len(r2)):
    y2.append(i)

print(r0[-1],r1[-1],r2[-1])
x=np.asanyarray(y0)
y=np.asanyarray(r0)
plt.plot(x,y)
plt.scatter(x, y)
plt.savefig('2-3-0.png')
plt.show()
x=np.asanyarray(y1)
y=np.asanyarray(r1)
plt.plot(x,y)
plt.scatter(x, y)
plt.savefig('2-3-1.png')
plt.show()

x=np.asanyarray(y2)
y=np.asanyarray(r2)
plt.plot(x,y)
plt.scatter(x, y)
plt.savefig('2-3-2.png')
plt.show()

print()


