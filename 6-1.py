import numpy as np
import matplotlib.pyplot as plt
import math

N = 1000
mu = 0.01


def f1(t, w1, w2):
    return w2


def f2(t, w1, w2):
    return mu * (1 - w1 * w1) * w2 - w1


def pt(res):
    plt.plot(np.array(res).T[0], np.array(res).T[1])
    plt.show()
    plt.plot(np.array(res).T[0], np.array(res).T[2])
    plt.show()

def RungeKutta2(a=0, b=10, n=N, alpha=1 , alpha1=0):
    h = (b - a) / n
    t = a
    w1 = alpha
    w2 = alpha1
    res=[[t,w1,w2]]
    for i in range(N):
        k11=h*f1(t,w1,w2)
        k12=h*f2(t,w1,w2)
        k21=h*f1(t+h/2,w1+k11/2,w2+k12/2)
        k22=h*f2(t+h/2,w1+k11/2,w2+k12/2)
        k31=h*f1(t+h/2,w1+k21/2,w2+k22/2)
        k32=h*f2(t+h/2,w1+k21/2,w2+k22/2)
        k41=h*f1(t+h/2,w1+k31/2,w2+k32/2)
        k42=h*f2(t+h/2,w1+k31/2,w2+k32/2)
        w1+=(k11+2*k21+2*k31+k41)/6
        w2+=(k12+2*k22+2*k32+k42)/6
        t+=h
        res.append([t,w1,w2])
    return res


res=RungeKutta2()
pt(res)