import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
from pylab import * 


class Occupations():
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
    
    def defineBreakDowns():
        data = open("IndustryBreakdowns/Industries.txt")
        dataList = data.read().split("\n")
        data.close()
        
        lineNum = 0
        currentIndustry = ""
        while lineNum < len(dataList):
            if ":" in dataList[lineNum]:
                currentIndustry = dataList[lineNum][:-1]
            else:
                if currentIndustry not in Industry.Breakdowns:
                    Industry.Breakdowns[currentIndustry] = {}
                thisLine = dataList[lineNum].split("   ")
                
                Industry.Breakdowns[currentIndustry][thisLine[1]] = float(thisLine[2])/100
            lineNum += 1
        
    
    def __init__(self, data, name):
        self.data = data
        self.name = name
        
    def plot(self):
        plt.plot(City.Years, self.data, label=self.name)
    
    def regression(self):
        if self.name not in ["Liverpool", "Barry"]:
            coef = np.polyfit(City.Years,self.data,1)
        else:
            coef = np.polyfit(City.Years[1:],self.data,1)
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
        
        if name not in ["Liverpool", "Barry"]:
            for industryIndex in range(len(self.table)):
                self.table[industryIndex] = self.table[industryIndex][:len(City.Years)]
        else:
            for industryIndex in range(len(self.table)):
                self.table[industryIndex] = self.table[industryIndex][:len(City.Years)-1]
                
        self.getFields()
            
    def getFields(self):
        self.industries = []
        for industryIndex in range(len(self.table)):
            self.industries.append(Industry(self.table[industryIndex], Industry.Industries[industryIndex]))
    
    def regression(self):
        self.linearFunctions = []
        for industry in self.industries:
            industry.regression()