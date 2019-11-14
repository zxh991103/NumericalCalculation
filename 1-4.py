import math
def f(x):
    return 2-3*x-math.sin(x)


print('prove:f(0)*f(1)=',f(0)*f(1),'<0')


x1=0
x2=1
i=0
while x2-x1>0.000005:
    i+=1
    x=(x1+x2)/2
    if f(x)*f(x1)<=0:
        x2=x
    else:
        x1=x

print(x1)


print(i)