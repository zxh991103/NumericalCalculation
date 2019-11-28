import numpy as np
import csv
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
x=x[0:11]
r=r[0:11]
p=p[0:11]
q=q[0:11]

x_r_p_q=np.array([x,r,p,q]).T

print(x_r_p_q)


t=[i for i in range(11)]

x_r=[(i[0]-i[1]) for i in x_r_p_q]
x_p=[(i[0]-i[2]) for i in x_r_p_q]
x_q=[-(i[0]-i[3]) for i in x_r_p_q]
result = open('data.xls', 'w', encoding='gbk')
result.write('X\tY\n')
for m in range(len(x_r_p_q)):
    for n in range(len(x_r_p_q[m])):
        result.write(str(x_r_p_q[m][n]))
        result.write('\t')
    result.write('\n')
result.close()

import matplotlib.pyplot as plt

plt.plot(t,x_r)
plt.scatter(t,x_r)


plt.show()
plt.plot(t,x_p)
plt.scatter(t,x_p)


plt.show()
plt.plot(t,x_q)
plt.scatter(t,x_q)


plt.show()


x_r_p_q=np.array([x_r,x_p,x_q]).T
result = open('data.xls', 'w', encoding='gbk')
result.write('X\tY\n')
for m in range(len(x_r_p_q)):
    for n in range(len(x_r_p_q[m])):
        result.write(str(x_r_p_q[m][n]))
        result.write('\t')
    result.write('\n')
result.close()