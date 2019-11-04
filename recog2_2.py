import os
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')



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
def drawcharacter(data):
     plt.plot(data[:,0],data[:,1])
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
    # drawcharacter(dataset[1])
    TestApp().run()
    