import numpy as np
from core.ComputeDistanceMatrix import *
from core.ComputeGap import *

def ComputeGapRaw(shapelets, dataset):
    dis, locations = ComputeDistanceMatrix(shapelets, dataset) 
    dis = np.real(dis)
    maxGap, dt, _ = ComputeGap(dis)

    return maxGap, dt, dis, locations