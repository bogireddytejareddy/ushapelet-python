#from core import *
import numpy as np
from sklearn import metrics
from FindFastUShapelet import *

dataFileName = '../UShapeletCode/TestingDatasets/Trace.txt'
data, classLabels = [], []

f = open(dataFileName, "r")
for x in f:
    tmp = []
    for num in x[2:-1].split(' '):
        tmp.append(float(num))
    data.append(tmp)
    classLabels.append(int(x[0]))

data = np.array(data)
classLabels = np.array(classLabels)

sLen = 30
allClassLabels = classLabels.copy()
minGap = 0
dataSize = data.shape[0]
uShapelets = []
gaps = []
remainingInd = np.array([idx for idx in range(dataSize)])
labelsResult = np.zeros((dataSize, 1))
currentClusterNum = 1
totalTime = 0

while (len(remainingInd) > 3):
    bestShIndex, bestShapelets, sLen, clsNum, _, _, _, _ = FindFastUShapelet(data, classLabels, dataFileName, sLen)

    maxGapCurrent = bestShapelets[bestShIndex, 2]
    _, _, newIDX = GetActualGap(sLen, bestShapelets, bestShIndex, data, classLabels, clsNum)

    ts = remainingInd[int(bestShapelets[bestShIndex, 0])]
    loc = bestShapelets[bestShIndex, 1]

    bsfUsh = [ts, loc, sLen, maxGapCurrent]
    bsfCurrentIDX = newIDX

    gaps.append(maxGapCurrent)
    if (minGap == 0):
        if (maxGapCurrent > 0):
            minGap = maxGapCurrent
        else:
            break
    else:
        if (minGap / 2 > maxGapCurrent):
            break
    
    indToDelete = np.argwhere(bsfCurrentIDX)

    data = np.delete(data, np.concatenate(indToDelete), axis=0)
    uShapelets.append(bsfUsh)
    
    if (len(classLabels) > 0):
        classLabels = np.delete(classLabels, np.concatenate(indToDelete), axis=0)

    labelsResult[remainingInd[indToDelete]] = currentClusterNum
    remainingInd = np.delete(remainingInd, np.concatenate(indToDelete), axis=0) 
    currentClusterNum = currentClusterNum + 1

resultRI = metrics.rand_score(allClassLabels, labelsResult[:, 0])
print('RI', resultRI)    
