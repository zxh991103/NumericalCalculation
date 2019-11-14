import numpy as np
r=[0.994]
p=[1,0.497]
q=[1,0.497]
x=[1]
for i in range(20):
    t=0.5*r[i]
    r.append(t)
    t=1.5*p[i+1]-0.5*p[i]
    p.append(t)
    t=2.5*q[i+1]-0.5*q[i]
    q.append(t)
    t=0.5*x[i]
    x.append(t)
print(q[2])
x=x[0:10]
r=r[0:10]
p=p[0:10]
q=q[0:10]

x_r_p_q=np.array([x,r,p,q]).T

print(x_r_p_q)

