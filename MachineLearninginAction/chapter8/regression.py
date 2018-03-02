from numpy import *
import os
import matplotlib.pyplot as plt

def loadDataSet(filename):
    with open(filename) as f:
        numFeat = len(f.readline().split('\t')) - 1
        f.seek(0)
        dataMat = []; labelMat = []
        for line in f.readlines():
            lineArr = []
            curLine = line.strip().split('\t')
            for i in range(numFeat):
                lineArr.append(float(curLine[i]))
            dataMat.append(lineArr)
            labelMat.append(float(curLine[-1]))
        return dataMat, labelMat

def standRegree(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0:
        print('This matrix is singular, cannot do inverse')
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws

filename = os.path.join(os.path.dirname(__file__), 'ex0.txt')
xArr, yArr = loadDataSet(filename)
xMat = mat(xArr); yMat = mat(yArr)
ws = standRegree(xArr, yArr)
'''
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xMat[:, 1].flatten().A[0], yArr)
xCopy = xMat.copy()
xCopy.sort(0)
yHat = xCopy * ws
ax.plot(xCopy[:, 1], yHat)
plt.show()
'''
def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))
    for j in range(m):
        diffMat = testPoint - xMat[j, :]
        weights[j, j] = exp(diffMat*diffMat.T / (-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0:
        print('This matrix is singular, cannot do inverse')
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws

def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat
'''
yHat = lwlrTest(xArr, xArr, yArr, 1)
strInd = xMat[:, 1].argsort(0)
xSort = xMat[strInd][:, 0, :]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xSort[:, 1], yHat[strInd])
plt.show()
'''
def rssError(yArr, yHatArr):
    return ((yArr - yHatArr)**2).sum()

def regularize(xMat):
    inMat = xMat.copy()
    inMeans = mean(inMat, 0)
    inVar = var(inMat, 0)
    inMat = (inMat - inMeans) / inVar
    return inMat

def stageWise(xArr, yArr, eps=0.01, numIt=100):
    xMat = mat(xArr); yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    xMat = regularize(xMat)
    m, n = shape(xMat)
    returnMat = zeros((numIt, n))
    ws = zeros((n, 1)); wsTest = ws.copy(); wsMax = ws.copy()
    for i in range(numIt):
        print(ws.T)
        lowestError = inf
        for j in range(n):
            for sign in [-1, 1]:
                wsTest = ws.copy()
                wsTest[j] += eps * sign
                yTest = xMat * wsTest
                resE = rssError(yMat.A, yTest.A)
                if resE < lowestError:
                    lowestError = resE
                    wsMax = ws
        ws = wsMax.copy()
        returnMat[i, :] = ws.T
    return returnMat





