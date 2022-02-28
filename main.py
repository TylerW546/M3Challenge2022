import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
from pylab import * 

from City import City

cities = ["Seattle", "Omaha", "Scranton", "Liverpool", "Barry"]

cityList = []



for city in cities:
    cityData = open("D1-Inputs/" + city + ".txt")
    cityInputString = cityData.read()
    cityData.close()
    
    cityList.append(City(city, cityInputString))


for fieldIndex in range(len(cityList[0].table)):
    plt.plot(City.Years, cityList[0].table[fieldIndex], label=City.Fields[fieldIndex])
    
plt.title("Avg number of Employees by industry")
plt.xlabel("Industry")
plt.ylabel("Employees")
plt.legend(loc="upper left")
plt.show()