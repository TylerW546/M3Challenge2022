from matplotlib.style import available
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
from pylab import * 
from City import *
#from RealRemoteWorkers import *

Occupations.defineOccupations()
Industry.defineBreakDowns()


cities = ["Seattle", "Omaha", "Scranton", "Liverpool", "Barry"]
# This will store City objects
cityList = []

yearMin = 2000
yearMax = 2030

# This is a dicitonary that will store one list of remote-ready workers for each year in the specified range 
availableWorkersPerCity = {}
# This is a dicitonary that will store one list of total workers for each year in the specified range
totalWorkersPerCity = {}

# Creating City objects based on their data (stored in text files) and adding them to cityList
for city in cities:
    cityData = open("D1-Inputs/" + city + ".txt")
    cityInputString = cityData.read()
    cityData.close()
    
    cityList.append(City(city, cityInputString))
    
# Plotting idustries
for city in cityList:
    for industry in city.industries:
        #industry.plot()
        industry.regression()
        #industry.plotApproxEmployees()

def predictedRemoteWorkersInYear(x, cityNum):
    totalRemoteWorkers = 0
    totalWorkers = 0
    for industry in cityList[cityNum].industries:
        totalWorkers+= industry.employeeFunction(x)
        for occupation in Industry.Breakdowns[industry.name]:
            totalRemoteWorkers += industry.employeeFunction(x) * Industry.Breakdowns[industry.name][occupation] * Occupations.OccupationDict[occupation]
    return totalRemoteWorkers, totalWorkers

def realRemoteWorkersInYear(x, cityNum):
    totalRemoteWorkers = 0
    totalWorkers = 0
    for industry in cityList[cityNum].industries:
        totalWorkers += industry.data[City.Years.index(x)]
        for occupation in Industry.Breakdowns[industry.name]:
            totalRemoteWorkers += industry.data[City.Years.index(x)] * Industry.Breakdowns[industry.name][occupation] * Occupations.OccupationDict[occupation]
    return totalRemoteWorkers, totalWorkers

def percentageRemoteInYear(year):
    percentWorkersRemote = []
    for city in range(5):
        remote, total = predictedRemoteWorkersInYear(year, city)
        percentWorkersRemote.append(remote/total)
    return percentWorkersRemote

print(percentageRemoteInYear(2021))

for year in range(yearMin, yearMax+1):
    remoteWorkersList = []
    totalWorkersList = []
    for city in range(5):
        remoteReady, totalWorkers = predictedRemoteWorkersInYear(year, city)
        remoteWorkersList.append(remoteReady)
        totalWorkersList.append(totalWorkers)
    availableWorkersPerCity[year] = remoteWorkersList
    totalWorkersPerCity[year] = totalWorkersList

global globalWorkersList
globalWorkersList = []

weightedAverageRemoteWorkers = {}
for year in range(yearMin, yearMax+1):
    totalWorkersList = totalWorkersPerCity[year]
    availableWorkersList = availableWorkersPerCity[year]
    
    totalWorkers = sum(totalWorkersList)
    globalWorkersList.append(totalWorkers)
    
    weightedAverageRemoteWorkers[year] = 0

    for i in range(5):
        weightedAverageRemoteWorkers[year] += availableWorkersList[i]
    weightedAverageRemoteWorkers[year]/=totalWorkers

percentageRemoteInYear(2021, )

def plotAverageRemoteWorkers():
    x = []
    y = []
    for i in range(yearMin, yearMax):
        x.append(i)
        y.append(weightedAverageRemoteWorkers[i])

    polyline = np.linspace(yearMin, yearMax, 50)
    plt.plot(x, y, label="Average Available Workers")
        
# plt.title("Avg number of Employees by industry")
# plt.xlabel("Industry")
# plt.ylabel("Employees")
# plt.legend(loc="upper left")
# plt.show()