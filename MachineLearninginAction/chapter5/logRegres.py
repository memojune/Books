import os
import random
from numpy import *

def loadDataSet():
    dataMat = []
    labelMat = []
    filename = os.path.join(os.path.dirname(__file__), 'testSet.txt')
    with open(filename) as fr:
        for line in fr:
            lineArr = line.strip().split()
            dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
            labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def sigmoid(inX):
    return 1 / (1 + exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    m, n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = labelMat - h
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights

def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat, labelMat = loadDataSet()
    n = len(dataMat)
    x1 = []; y1 = []
    x2 = []; y2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            x1.append(dataMat[i][1]); y1.append(dataMat[i][2])
        else:
            x2.append(dataMat[i][1]); y2.append(dataMat[i][2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x1, y1, s=30, c='red', marker='s')
    ax.scatter(x2, y2, s=30, c = 'green')
    x = arange(-3, 3, 0.1)
    y = (-weights[0] - weights[1]*x) / weights[2]
    ax.plot(x, y)
    plt.show()

def stocGradAscent(dataMatrix, classLabels, numIter=150):
    m, n = shape(dataMatrix)
    weights = ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4 / (1 + i + j) + 0.01
            indexOfDataIndex = int(random.uniform(0, len(dataIndex)))
            randomIndex = dataIndex[indexOfDataIndex]
            h = sigmoid(sum(dataMatrix[randomIndex] * weights))
            error = classLabels[randomIndex] - h
            weights = weights + alpha * error * dataMatrix[randomIndex]#  a*list != a*array 前者扩展List 后者与元素相乘
            del(dataIndex[indexOfDataIndex])
    return weights


