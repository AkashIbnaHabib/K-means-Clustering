import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
import os



trainSet = pd.read_csv('data.txt', sep = " ", header=None, dtype='float64')


trainArr = trainSet.values

trainArrLen = trainArr[ : , 0 ].size




classArr = []

for i in range( trainArrLen) :

        classArr.extend([trainArr[i,0:2]])



classArr = np.array(classArr)


classLen=classArr[:,0].size

print(classLen,trainArrLen)


classXvalues = classArr[:,0]

classYvalues = classArr[:,1]

xmin = np.min(classXvalues)
xmax = np.max(classXvalues)
ymin = np.min(classYvalues)
ymax = np.max(classYvalues)


figure,axes = plt.subplots(1,2)

axes[0].scatter(classXvalues,classYvalues, label = 'All Data',color='g',marker='+')
axes[0].set_xlabel('X-axis')
axes[0].set_ylabel('Y-axis')
axes[0].set_title('Original Data')
axes[0].legend()


k = int(input("Input cluster number: "))

random.seed(30)

cenX=[]
cenY = []
colorA = []


for i in range(k):
    cenX.extend([random.uniform(xmin,xmax)])
    cenY.extend([random.uniform(ymin,ymax)])
    colorA.append(np.random.rand(3, ))

cenX = np.array(cenX)
cenY = np.array(cenY)


print(cenX)

print(cenY)



iteration = 0

while iteration!=80:

    count=0

    for i in range(classLen):
        dist = []
        for j in range(k):
            dist.extend([math.sqrt(((classArr[i, 0] - cenX[j]) ** 2) + ((classArr[i, 1] - cenY[j]) ** 2))])
            

        ind = np.argmin(dist)
       
        ind=ind+1
        file = open("cluster" + str(ind) + ".txt", "a")
        file.write(f"{round(classArr[i, 0],4)},{round(classArr[i, 1],4)}\n")
        file.close()




    for i in range(k):
        clusterS = pd.read_csv("cluster" + str(i + 1) + ".txt", sep=",", header=None)
        clusterSet=clusterS.values

        clusterSet = np.array(clusterSet)

        clusterSetXavg = np.mean(clusterSet[:, 0])
        clusterSetYavg = np.mean(clusterSet[:, 1])
        if (clusterSetXavg != cenX[i]) or (clusterSetYavg != cenY[i]):
            cenX[i]=clusterSetXavg
            cenY[i]=clusterSetYavg
        else:
            count=count+1

    
    if count==k:
        
        break
    else:
        for i in range(k):
            os.remove("cluster" + str(i+1) + ".txt")
    iteration=iteration+1

    print("iteration: ",iteration)




markerA = ['s','H','2','X','o','p']


for i in range(k):
    plotS = pd.read_csv("cluster" + str(i + 1) + ".txt", sep=",", header=None)
    plotSet = plotS.values
    axes[1].scatter(plotSet[:, 0], plotSet[:, 1], label="cluster " + str(i + 1), color=colorA[i], marker=markerA[i])
    axes[1].set_xlabel('X-axis')
    axes[1].set_ylabel('Y-axis')
    axes[1].set_title('After Clustering')
    axes[1].legend()
   

plt.show()


