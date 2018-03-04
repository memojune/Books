from numpy import *
import os
import matplotlib.pyplot as plt

def loadData(filename):
    dataMat = []
    with open(filename) as f:
        for line in f.readlines():
            curLine = line.strip().split('\t')
            fltLine = list(map(float, curLine))
            dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

def randCent(dataSet, k):
    m, n = shape(dataSet)
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j]) - minJ)
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids
'''
filename = os.path.join(os.path.dirname(__file__), 'testSet.txt')
myData = loadData(filename)
myMat = mat(myData)
filename2 = os.path.join(os.path.dirname(__file__), 'testSet2.txt')
myData2 = loadData(filename2)
myMat2 = mat(myData2)
'''
def kMeans(dataSet, k, distMeans=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeans(centroids[j], dataSet[i])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids.A, clusterAssment
'''
myCentroids, clusteAssing = kMeans(myMat, 4)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(myCentroids[:, 0].T.A, myCentroids[:, 1].T.A, c='red')
ax.scatter(myMat[:, 0].T.A, myMat[:, 1].T.A)
plt.show()
'''
def biKmeans(dataSet, k, distMens=distEclud):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroid0 = mean(dataSet, axis=0).tolist()[0]
    centList = [centroid0]
    for j in range(m):
        clusterAssment[j, 1] = distMens(mat(centroid0), dataSet[j, :])**2
    while(len(centList) < k):
        lowestSSE = inf
        for i in range(len(centList)):
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:, 0].A == i)[0]]
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMens)
            sseSplit = sum(splitClustAss[:, 1])
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:, 0].A != i)[0], 1])
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(centList)
        bestClustAss[nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentToSplit
        centList[bestCentToSplit] = bestNewCents[0]
        centList.append(bestNewCents[1])
        clusterAssment[nonzero(clusterAssment[:, 0].A == bestCentToSplit)[0]] = bestClustAss
    return mat(centList), clusterAssment
'''
myCentroids, clusteAssing = biKmeans(myMat2, 3)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(myMat2[:, 0].T.A, myMat2[:, 1].T.A)
ax.scatter(myCentroids[:, 0].T.A, myCentroids[:, 1].T.A, c='red')
plt.show()
'''
filename = 'D:\CS\python\MLA\chapter10\Portland.png'
fig = plt.figure()
rect = [0.1, 0.1, 0.4, 0.4]
ax0 = fig.add_axes(rect ,label='ax0')
imgP = plt.imread(filename)
ax0.imshow(imgP)
plt.show()
