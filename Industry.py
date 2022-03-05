import matplotlib.pyplot as plt
import numpy as np

Years = [2000, 2005, 2010, 2015, 2019]

class Industry:
    Industries = [
        "Mining, logging, construction",
        "Manufacturing",
        "Trade, transportation, and utilities",
        "Information",
        "Financial activities",
        "Professional and business services",
        "Education and health services",
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

    def __init__(self, data, name, cityName):
        self.data = data
        self.name = name
        self.cityName = cityName
        
    def plot(self, label=None):
        if label == None:
            label=self.name
        if self.cityName not in ["Liverpool", "Barry"]:
            plt.plot(Years, self.data, label=label)
        else:
            plt.plot(Years[1:], self.data, label=label)
    
    def regression(self):
        if self.cityName not in ["Liverpool", "Barry"]:
            coef = np.polyfit(Years,self.data,1)
        else:
            coef = np.polyfit(Years[1:],self.data,1)
        self.employeeFunction = np.poly1d(coef)

    def plotApproxEmployees(self, yearMin, yearMax, label=None):
        plt.plot([yearMin, yearMax], self.employeeFunction([yearMin, yearMax]), '--k', label=label)