from matplotlib.style import available
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
from pylab import * 
from City import *
import math
#from RealRemoteWorkers import *

Occupations.defineOccupations()
Industry.defineBreakDowns()

cities = ["Seattle", "Omaha", "Scranton", "Liverpool", "Barry"]

# This will store the 5 City objects once they are made
cityList = []

# These specify the range of years that the data will extrapolate over 
yearMin = 2000
yearMax = 2030

# This is a dicitonary that will store one list of remote-ready workers for each year in the specified range. The list contains 5 values, one for each city
readyWorkersPerCity = {}
# This is a dicitonary that will store one list of total workers for each year in the specified range. The list contains 5 values, one for each city
totalWorkersPerCity = {}

# Creating City objects based on their data (stored in text files) and adding them to cityList
# These text files are not included in this appendix as they are simply the tables copied from the D1 spreadsheet
# the naming convention for these files is cityName.txt. For example: Seattle.txt, and they were stored in a file called D1-Inputs.
for city in cities:
    cityData = open("D1-Inputs/" + city + ".txt")
    cityInputString = cityData.read()
    cityData.close()
    
    # Create the object with the data
    cityList.append(City(city, cityInputString))
    
# Calculating idustry growth. This is handled in the Industry objects
for city in cityList:
    for industry in city.industries:
        industry.regression()

# Plotting industry growth of Government in Seattle
# Seattle is city 0
# Government is industry 9
cityList[0].industries[9].plot("Government Industry in Seattle DATA")
cityList[0].industries[9].plotApproxEmployees(2000,2030, "Government Industry in Seattle PREDICTION")
plt.title("Avg number of Employees in Government in Seattle Per Year")
plt.legend(loc="lower left")
plt.xlabel("Year")
plt.ylabel("Employees")
plt.ylim(0,1.2*max(cityList[0].industries[9].employeeFunction(yearMax),cityList[0].industries[9].employeeFunction(yearMin)))
plt.show()


# Plotting all 10 industries' growth in Barry
for industry in cityList[4].industries:
    industry.plot()
    industry.plotApproxEmployees(2005,2030)
plt.title("Avg number of Employees in Seattle In Various Industries Per Year")
plt.legend(loc="upper left")
plt.xlabel("Year")
plt.ylabel("Employees")
plt.show()

def predictedRemoteWorkersInYear(year, cityNum):
    '''Given a year and city, return the predicted number of remote-ready jobs'''
    totalRemoteWorkers = 0
    totalWorkers = 0
    # Loop over every industry in the city
    for industry in cityList[cityNum].industries:
        # Add the value the regression model (employeeFunction) returns for this industry on that year
        totalWorkers += industry.employeeFunction(year)
        
        # Run through the occupations within the given idustry
        for occupation in Industry.Breakdowns[industry.name]:
            # Preform the multiplication described in 2.3.2
            totalRemoteWorkers += industry.employeeFunction(year) * Industry.Breakdowns[industry.name][occupation] * Occupations.OccupationDict[occupation]
    return totalRemoteWorkers, totalWorkers

def realRemoteWorkersInYear(year, cityNum):
    '''Given a year and city, return the predicted number of remote-ready jobs'''
    totalRemoteWorkers = 0
    totalWorkers = 0
    # Loop over every industry in the city
    for industry in cityList[cityNum].industries:
        # Make sure that Liverpool and Barry don't try to use 2000 as they don't have data for that year
        if cityNum > 2:
            realData = industry.data[City.Years[1:].index(year)]
        else:
            realData = industry.data[City.Years.index(year)]
        
        # Add the real number to the total workers
        totalWorkers += realData
        
        # Use occuptaions as previously described
        for occupation in Industry.Breakdowns[industry.name]:
            totalRemoteWorkers += realData * Industry.Breakdowns[industry.name][occupation] * Occupations.OccupationDict[occupation]
    return totalRemoteWorkers, totalWorkers

def percentageRemoteInYear(year, city):
    '''From a given year and city, return remote-ready jobs / all jobs'''
    remote, total = predictedRemoteWorkersInYear(year, city)
    return remote/total

def percentError(years):
    '''Calculate the % error of a set of years'''
    error = 0
    totalReal = 0
    # Sum up total and error values across years and cities
    for year in years:
        for city in range(5):
            totalReal += realRemoteWorkersInYear(year,city)[0]
            error += abs(predictedRemoteWorkersInYear(year, city)[0]-realRemoteWorkersInYear(year,city)[0])
    # Error/total = % Error
    return error/totalReal

# Print Q1 Answers
print("\n\n\nRemote-Ready Percentages in Seattle, Omaha, Scranton, Liverpool, and Barry over years 2021, 2024, 2027")
for year in [2021, 2024, 2027]:
    for city in range(5):
        print(percentageRemoteInYear(year, city), end="")
    print()
print("Percent Error:" + str(int(percentError([2005,2010,2015,2019])*10000)/100))
print("\n\n\n")


# --------------- Information for Q2 ---------------

# For each year in the range, find the remote-ready and total workers in each city
for year in range(yearMin, yearMax+1):
    remoteWorkersList = []
    totalWorkersList = []
    for city in range(5):
        remoteReady, totalWorkers = predictedRemoteWorkersInYear(year, city)
        remoteWorkersList.append(remoteReady)
        totalWorkersList.append(totalWorkers)
    readyWorkersPerCity[year] = remoteWorkersList
    totalWorkersPerCity[year] = totalWorkersList

# For each year, go through and find the weightedGlobalPercentageRemoteWorkers

# This is the global average of Remote Workers, taking population into account when averaging
# Essentially, with more population, a city's value will change the average more
weightedGlobalPercentageRemoteWorkers = {}
for year in range(yearMin, yearMax+1):
    totalWorkersList = totalWorkersPerCity[year]
    readyWorkersList = readyWorkersPerCity[year]

    totalWorkers = sum(totalWorkersList)
    weightedGlobalPercentageRemoteWorkers[year] = 0
    for i in range(5):
        weightedGlobalPercentageRemoteWorkers[year] += percentageRemoteInYear(year, i) * totalWorkersList[i]/totalWorkers


def getGlobalReadyWorkerPercentage():
    '''Return a list of y values for the previously calculated dictionary weightedGlobalPercentageRemoteWorkers'''
    y = []
    for i in range(yearMin, yearMax+1):
        y.append(weightedGlobalPercentageRemoteWorkers[i]*100)
    return y

def plotAverageRemoteWorkers():
    '''Plots weightedGlobalPercentageRemoteWorkers'''
    x = []
    y = []
    for i in range(yearMin, yearMax+1):
        x.append(i)
        y.append(weightedGlobalPercentageRemoteWorkers[i]*100)

    polyline = np.linspace(yearMin, yearMax, 50)
    plt.plot(x, y, label="Average Available Workers")