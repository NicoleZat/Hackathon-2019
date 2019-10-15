import plotly.graph_objects as go
import pandas as pd
import numpy as np

#Non class specific function
def isAboveLine(x, y, m, b): #BUG: all the line stuff is garbage, make it dynamic and make classification work properly
    return ((m)*(x-105) - y + b + 85) < 0

#Example Data sets imported from actual LR model
class Example :
    def __init__(self):
        self.hX = []
        self.hY = []
        self.sX = []
        self.sY = []

    #Load all data into the arrays
    def initData(self, csv_loc):
        allData = pd.read_csv(csv_loc)
        for i in range(len(allData)):
            if(allData['sepsis'][i] == 1):
                self.sX.append(allData['temperature'][i])
                self.sY.append(allData['pulse'][i])
            else:
                self.hX.append(allData['temperature'][i])
                self.hY.append(allData['pulse'][i])
        print(self.hX)

    def getHealthyXData(self):
        return self.hX

    def getHealthyYData(self):
        return self.hY

    def getSepsisXData(self):
        return self.sX

    def getSepsisYData(self):
        return self.sY

    def getDBx(self): #TODO: make this dynamic to the data set
        return np.linspace(90, 115);

    def getDBy(self, m, b):
        allYs = []
        X = np.linspace(90,115);
        for x in X:
            allYs.append(m*(x-105) + b + 85)
        return allYs

    def getPieVector(self, m, b):
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        #Go through all 4 data types
        for h in range(len(self.hX)):
            if(isAboveLine(self.hX[h], self.hY[h], m, b)):
                FP += 1
            else:
                TN += 1
        for s in range(len(self.sX)):
            if(isAboveLine(self.sX[s], self.sY[s], m, b)):
                TP += 1
            else:
                FN += 1
        #Return vector
        return [TP, TN, FP, FN]

    def getPieLabels(self):
        return ["True Pos", "True Neg", "False Pos", "False Neg"]
