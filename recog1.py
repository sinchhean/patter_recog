import os
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier

#path to walking sitting and jogging respectively
path1 = "./data/act01/"
path2 = "./data/act02/"
path3 = "./data/act03/"

testpath = "./data/test/"

#variables for all  walking sitting and jogging files data and its rms etc
walk = []
sit = []
jog = []
walkRMS = []
jogRMS = []
jogRMS = []
testdata = []
testdataRMS = []
target = []
resultPrediction = []

#rms
def rms(array):
   return np.sqrt(np.mean(array ** 2))

#rms for each axis 
def findRMS(array,text = None):
    global target
    dRMS = []
    for items in array:
        dRMS.append([rms(items[:,0]),rms(items[:,1]),rms(items[:,2])])
        if text != None:
            target.append(text)
    return dRMS

#read files from each action and put into an array
def readFilesintoArray(path):
    darray = []
    for filename in os.listdir(path):
        darray.append(np.loadtxt(fname=path+filename))
    return darray

#ploting seperate by row
def plotdata(data,filenumber):
    plt.plot(data[filenumber-1][:,0],label="x") 
    plt.plot(data[filenumber-1][:,1],label="y")
    plt.plot(data[filenumber-1][:,2],label="z")
    plt.legend()
    plt.show()

#3D plot
def threeDplot(data1,data2,data3):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data1[:,0],data1[:,1],data1[:,2],label="walking")
    ax.scatter(data2[:,0],data2[:,1],data2[:,2],label="sitting")
    ax.scatter(data3[:,0],data3[:,1],data3[:,2],label="jogging")
    ax.set_xlabel('X-coo')
    ax.set_ylabel('Y-coo')
    ax.set_zlabel('Z-coo')
    plt.legend()
    plt.show()   

#KNN classifier model
def knnModelPredict(data,testdata):
    global target
    knn = KNeighborsClassifier(n_neighbors=7)
    knn.fit(data,target)
    return knn.predict(testdata)


if __name__ == "__main__":
    walk = np.array(readFilesintoArray(path1))
    sit = np.array(readFilesintoArray(path2))
    jog = np.array(readFilesintoArray(path3))

    plotdata(walk,1)

    walkRMS = np.array(findRMS(walk,text="walk"))
    sitRMS = np.array(findRMS(sit,text="sit"))
    jogRMS = np.array(findRMS(jog,text="jog"))
    
    # threeDplot(walkRMS,sitRMS,jogRMS)

    traindata = np.concatenate((walkRMS,sitRMS,jogRMS),axis = 0)
    testdata = np.array(readFilesintoArray(testpath))
    testdataRMS = np.array(findRMS(testdata))
    
    resultPrediction = knnModelPredict(traindata,testdataRMS)
    print(resultPrediction)