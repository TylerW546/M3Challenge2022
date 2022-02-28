import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
from pylab import * 

from City import *

Occupations.defineOccupations()

cities = ["Seattle", "Omaha", "Scranton", "Liverpool", "Barry"]

cityList = []


# Making City objects
for city in cities:
    cityData = open("D1-Inputs/" + city + ".txt")
    cityInputString = cityData.read()
    cityData.close()
    
    cityList.append(City(city, cityInputString))

# Plotting Seattles idustries
for industry in cityList[0].industries:
    industry.plot()
    industry.regression()
    industry.plotApproxEmployees()

def predictedRemoteWorkersInYear(x):
    totalRemoteWorkers = 0
    for industry in cityList[0].industries:
        for occupation in Industry.Breakdowns[industry.name]:
            totalRemoteWorkers += industry.employeeFunction(x) * Industry.Breakdowns[industry.name][occupation] * Occupations.OccupationDict[occupation]
        

    
plt.title("Avg number of Employees by industry")
plt.xlabel("Industry")
plt.ylabel("Employees")
plt.legend(loc="upper left")
plt.show()