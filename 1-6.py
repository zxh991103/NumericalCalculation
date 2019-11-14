import math

def f(x):
    return 5*x-math.exp(x)

#二分法

x1=0
x2=1
while x2-x1>0.0001:
    x=(x1+x2)/2
    if f(x)*f(x1)<=0:
        x2=x
    else:
        x1=x

print('二分结果:',(x1+x2)/2)


#牛顿法


delta = 0.000001

def f_1(x):
    return (f(x+delta)-f(x))/delta
def g(x):
    return x-f(x)/f_1(x)

def cal(x0):
    res=[0,x0]
    t1=0
    t2=x0
    while ( abs( t1-t2 ) > pow(10,-4) ):
        t1=t2
        t2=g(res[len(res)-1])
        res.append(t2)
    return res

res=cal(1)
print('牛顿法:',res[-1])


#割线法


def cut():
    t1=0
    t2=0.1
    res=[t1,t2]
    while abs(t2-t1) > pow(10,-4):
        temp=t2
        t2= t2-( f(t2)*(t2-t1) )/( f(t2) - f(t1) )
        t1=temp
        res.append(t2)

    return res

res1=cut()

print('割线法:',res1[-1])


#错位法



def dislocation():
    t1 = 0
    t2 = 0.3

    while abs(t2-t1) > 0.0001:
        t = t2 - (f(t2)*(t2-t1))/(f(t2)-f(t1))
        if f(t) * f(t1) <= 0:
            t2 = t
        else:
            t1 = t
        # print((t1+t2)/2)
    return (t1+t2)/2

print('错位法:',dislocation())



