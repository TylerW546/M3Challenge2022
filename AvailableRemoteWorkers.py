import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
from pylab import * 
from City import *
from RealRemoteWorkers import *

Occupations.defineOccupations()
Industry.defineBreakDowns()

cities = ["Seattle", "Omaha", "Scranton", "Liverpool", "Barry"]

cityList = []


# Making City objects
for city in cities:
    cityData = open("D1-Inputs/" + city + ".txt")
    cityInputString = cityData.read()
    cityData.close()
    
    cityList.append(City(city, cityInputString))

cityNum = 1

# Plotting idustries
for industry in cityList[cityNum].industries:
    industry.plot()
    industry.regression()
    industry.plotApproxEmployees()

def predictedRemoteWorkersInYear(x):
    totalRemoteWorkers = 0
    totalWorkers = 0
    for industry in cityList[cityNum].industries:
        totalWorkers+= industry.employeeFunction(x)
        for occupation in Industry.Breakdowns[industry.name]:
            totalRemoteWorkers += industry.employeeFunction(x) * Industry.Breakdowns[industry.name][occupation] * Occupations.OccupationDict[occupation]
    return totalRemoteWorkers,totalWorkers

def realRemoteWorkersInYear(x):
    totalRemoteWorkers = 0
    totalWorkers = 0
    for industry in cityList[cityNum].industries:
        totalWorkers += industry.data[City.Years.index(x)]
        for occupation in Industry.Breakdowns[industry.name]:
            totalRemoteWorkers += industry.data[City.Years.index(x)] * Industry.Breakdowns[industry.name][occupation] * Occupations.OccupationDict[occupation]
    return totalRemoteWorkers, totalWorkers

# for year in City.Years:
#     print(predictedRemoteWorkersInYear(year))
#     print(realRemoteWorkersInYear(year))

remoteJobs, allJobs = predictedRemoteWorkersInYear(2005)
print(remoteJobs/allJobs)

plt.title("Avg number of Employees by industry")
plt.xlabel("Industry")
plt.ylabel("Employees")
plt.legend(loc="upper left")
plt.show()