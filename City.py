import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
from pylab import * 
from Industry import Industry
from Occupations import Occupations

class City:
    Years = [2000, 2005, 2010, 2015, 2019]#, 2020, 2021]
    
    def __init__(self, name, inputString):
        self.table = []
        self.name = name
        
        self.table = inputString.split("\n")
        for i in range(len(self.table)):
            self.table[i] = self.table[i].split("\t")
            for j in range(len(self.table[i])):
                self.table[i][j] = int(self.table[i][j])
        
        if self.name not in ["Liverpool", "Barry"]:
            for industryIndex in range(len(self.table)):
                self.table[industryIndex] = self.table[industryIndex][:len(City.Years)]
        else:
            for industryIndex in range(len(self.table)):
                self.table[industryIndex] = self.table[industryIndex][:len(City.Years)-1]
                
        self.getIndustries()
            
    def getIndustries(self):
        self.industries = []
        for industryIndex in range(len(self.table)):
            self.industries.append(Industry(self.table[industryIndex], Industry.Industries[industryIndex], self.name))
    
    def regression(self):
        self.linearFunctions = []
        for industry in self.industries:
            industry.regression()