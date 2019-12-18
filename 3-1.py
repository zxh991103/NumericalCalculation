import cv2
import matplotlib.pyplot as plt
import numpy as np
path="D:\\jm2001A\\cumcm2001a-bmp"

pic=[]

for i in range(100):
    pic.append(cv2.imread(path+"\\"+str(i)+".bmp"))

print(pic[0][0][0]) #100 * 512*512*3

zos=np.zeros((512,512))

pic1=[]
for i in range(100):
    zos = np.zeros((512, 512))
    for j in range(512):
        for k in range(512):
            if pic[i][j][k][0]!=255 or pic[i][j][k][1]!=255 or pic[i][j][k][2]!=255:
                zos[j][k]=1
    pic1.append(zos)


points=[]
for k in range(100):
    from sklearn.cluster import KMeans
    temp=[]
    for i in range(512):
        for j in range(512):
            if pic1[k][i][j]==1:
                temp.append([i,j])
    kmeans = KMeans(init='k-means++', n_clusters=1, n_init=10)
    kmeans.fit(temp)
    points.append(kmeans.cluster_centers_[0])
    print(k)


points3D=[]
k=1
for i in points:
    points3D.append([i[0],i[1],k*1.0])
    k+=1



import matplotlib.pyplot as plt
import matplotlib.cm as cmx
from mpl_toolkits.mplot3d import Axes3D


pT=np.array(points3D).T
fig = plt.figure()
ax = fig.gca(projection='3d') # 得到3d坐标的图
cm = plt.cm.get_cmap('RdYlBu')
ax.view_init(45, 60)
sc=ax.scatter(pT[0], pT[1], pT[2],c=pT[2], vmin=0, vmax=100, s=35, cmap=cm)
plt.colorbar(sc)
plt.savefig('2001_0.png')
plt.show()


plt.plot(pT[0],pT[1])
plt.savefig('2001_1.png')
plt.show()


plt.plot(pT[0],pT[2])
plt.savefig('2001_2.png')
plt.show()


plt.plot(pT[1],pT[2])
plt.savefig('2001_3.png')
plt.show()


#x ~ y
import numpy as np
import matplotlib.pyplot as plt
x = pT[0]
x = np.array(x)
num = pT[1]
y = np.array(num)
f1 = np.polyfit(x, y, 8)
p1 = np.poly1d(f1)
print('p1 is :\n',p1)
#也可使用yvals=np.polyval(f1, x)
yvals = p1(x)#拟合y值
#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('polyfitting')
plt.savefig('2001_4.png')
plt.show()


# x ~ z
import numpy as np
import matplotlib.pyplot as plt
x = pT[0]
x = np.array(x)
num = pT[2]
y = np.array(num)
f1 = np.polyfit(x, y, 8)
p1 = np.poly1d(f1)
print('p1 is :\n',p1)
#也可使用yvals=np.polyval(f1, x)
yvals = p1(x)#拟合y值
#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('polyfitting')
plt.savefig('2001_5.png')
plt.show()