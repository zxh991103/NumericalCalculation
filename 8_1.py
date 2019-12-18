import numpy as np





a = [
    [1, -1, 1],
    [1, -0.5, 0.25],
    [1, 0, 0],
    [1, 0.5, 0.25],
    [1, 1, 1]
]
b = [1, 0.5, 0, 0.5, 2]
I = np.eye(5)

A = np.array(a).T
B = np.array(b).T


def vvt(v):
    res = np.zeros((len(v),len(v)))
    for i in range(len(v)):
        for j in range(len(v)):
            res[i][j] = v[i] * v[j]
    return res



def vtv(v):
    sum = 0
    for i in range(len(v)):
            sum  += v[i] * v[i]
    return sum

def vvt1(v):
    return vvt(v)/vtv(v)


def H(v):
    I=np.eye(len(v))
    H=I-2*vvt1(v)
    return H

def HA(v,A):
    return np.matmul(H(v),A.T)

def HB(H,B):
    return np.matmul(H,B)


def createv(A,A0,k,j):
    s1=0
    for i in range(k,len(A0[k])):
        s1+=pow(A0[k][i],2)
    s1=pow(s1,0.5)
    res=[]
    for fk in A[k]:
        res.append(fk)
    for i in range(j):
        res[i]=0
    if A[k][j]>0:
        res[j]+=s1
    else:
        res[j]-=s1
    return res
v1=createv(A,A,0,0)
H1=H(v1)
A1=np.array(HA(v1,A))
print(A1)
A1=A1.T
v2=createv(A1,A,1,1)
H2=H(v2)
A2=np.array(HA(v2,A1))
print(A2)
A2=A2.T
v3=createv(A2,A,2,2)
H3=H(v3)
A3=HA(v3,A2)
print(A3)


B1=HB(H1,B)
print(B1)
B2=HB(H2,B1)
print(B2)
B3=HB(H3,B2)
print(B3)


print(H1)
print(H2)
print(H3)


for i in B3:
    i=np.array([i])
    for j in range(len(i)):
        if j != len(i)-1:
            print('{'+str(i[j])[0:7]+'}',end='&')
        else:
            print('{' + str(i[j])[0:7] + '}',end='')
            print('\\\\')