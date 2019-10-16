import os
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier

#path to data
datapath = "./SignatureSampleData/"


#variables
dataset = []



#read files from each action and put into an array
def readFilesintoArray(path):
    darray = []
    for filename in os.listdir(path):
        darray.append(np.loadtxt(fname=path+filename,skiprows=1))
    return darray

#ploting seperate by row
def plotdata(data,filenumber):
    plt.subplot(6,1,1)
    plt.plot(data[filenumber-1][:,5],data[filenumber-1][:,0]) 
    plt.xlabel("time (s)")
    plt.ylabel("x-coor")
    plt.subplot(6,1,2)
    plt.plot(data[filenumber-1][:,5],data[filenumber-1][:,1])
    plt.xlabel("time (s)")
    plt.ylabel("y-coor")
    plt.subplot(6,1,3)
    plt.plot(data[filenumber-1][:,5],data[filenumber-1][:,2])
    plt.xlabel("time (s)")
    plt.ylabel("pressure")
    plt.subplot(6,1,4)
    plt.plot(data[filenumber-1][:,5],data[filenumber-1][:,3])
    plt.xlabel("time (s)")
    plt.ylabel("azimuth")
    plt.subplot(6,1,5)
    plt.plot(data[filenumber-1][:,5],data[filenumber-1][:,4])
    plt.xlabel("time (s)")
    plt.ylabel("altitude")
    plt.show()

#3D plot
def threeDplot(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:,0],data[:,1],data[:,5])
    ax.set_xlabel('X-coo')
    ax.set_ylabel('Y-coo')
    ax.set_zlabel('Z-coo')
    plt.show()   


if __name__ == "__main__":
    dataset = np.array(readFilesintoArray(datapath))
    for j,data in enumerate(dataset):
        rowtodel = []
        for i,arr in enumerate(data):
            if(arr[0] == -1):
                rowtodel.append(i)
        dataset[j] = np.delete(dataset[j],rowtodel,axis=0)       
    # plotdata(dataset,1)
    threeDplot(dataset[0])