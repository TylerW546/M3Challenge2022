import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
from pylab import * 


class Occupations():
    Occupations = [
        "Computer and mathematical",
        "Education, training and library",
        "Legal",
        "Business and financial operations",
        "Management",
        "Arts, design, entertainment, sports and media",
        "Office and administrative",
        "Architecture and engineering",
        "Life, physical and social science",
        "Community and social service",
        "Sales and related",
        "Personal care and service",
        "Protective service",
        "Healthcare practitioners and technical",
        "Transportation and material moving",
        "Healthcare support",
        "Farming, fishing and forestry",
        "Production",
        "Installation, maintenance and repair",
        "Construction and extraction",
        "Food preparation and service related",
        "Building and grounds cleaning and maintenance"]
    
    OccupationDict = {}
    
    def defineOccupations():
        data = open("D3-Inputs/HomeWorkPerJob.txt")
        dataString = data.read().split("\n")
        data.close()
        
        for i in range(len(dataString)):
            dataString[i] = dataString[i].split("\t")
            
        for occupationLine in dataString:
            Occupations.OccupationDict[occupationLine[0]] = float(occupationLine[1][:-1])/100



class Industry:
    Industries = [
        "Mining, logging, construction",
        "Manufacturing",
        "Trade, transportation, and utilities",
        "Information",
        "Financial activities",
        "Professional and business services",
        "Education and health services",
        "Information",
        "Leisure and hospitality",
        "Other services",
        "Government"]
    
    Breakdowns = {}
    
    def __init__(self, data, name):
        self.data = data
        self.name = name
        
    def plot(self):
        plt.plot(City.Years, self.data, label=self.name)
    
    def regression(self):
        coef = np.polyfit(City.Years,self.data,1)
        self.employeeFunction = np.poly1d(coef)

    def plotApproxEmployees(self):
        plt.plot(City.Years, self.data, 'yo', City.Years, self.employeeFunction(City.Years), '--k')

        


class City:
    Years = [2000, 2005, 2010, 2015, 2019]#, 2020, 2021]
    
    def __init__(self, name, inputString):
        self.table = []
        
        self.table = inputString.split("\n")
        for i in range(len(self.table)):
            self.table[i] = self.table[i].split("\t")
            for j in range(len(self.table[i])):
                self.table[i][j] = int(self.table[i][j])
        
        for industryIndex in range(len(self.table)):
            self.table[industryIndex] = self.table[industryIndex][:len(City.Years)]
        
        self.getFields()
            
    def getFields(self):
        self.industries = []
        for industryIndex in range(len(self.table)):
            self.industrys.append(Industry(self.table[industryIndex], City.IndusIndustriestry[industryIndex]))
    
    def regression(self):
        self.linearFunctions = []
        for industry in self.industries:
            industry.regression()
            

            
        
        
        
        
        


  
      