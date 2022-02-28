import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

from City import City

cities = ["Seattle", "Omaha", "Scranton", "Liverpool", "Barry"]

cityList = []



for city in cities:
    cityData = open("/D1-Inputs/" + city + ".txt")
    cityString = cityData.read()
    cityData.close()
    
    cityList.append(cityString)
    
