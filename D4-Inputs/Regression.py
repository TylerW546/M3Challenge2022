import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

date  = []
percentHome = []

with open('Post-Covid.txt') as f:
    lines = f.readline().split()
    while lines:
        print(lines)
        date.append(int(lines[0]))
        percentHome.append(float(lines[1][0 : len(lines[1])-2]))
        lines = f.readline().split()

f.close()

print(date)
print(percentHome)





#add legend
hours = [6, 9, 12, 12, 15, 21, 24, 24, 27, 30, 36, 39, 45, 48, 57, 60]
happ = [12, 18, 30, 42, 48, 78, 90, 96, 96, 90, 84, 78, 66, 54, 36, 24]

import matplotlib.pyplot as plt

#create scatterplot
plt.scatter(date, percentHome)

#polynomial fit with degree = 2
model = np.poly1d(np.polyfit(date, percentHome, 2))

#add fitted polynomial line to scatterplot
polyline = np.linspace(2000, 2030, 50)
plt.scatter(date, percentHome)
plt.plot(polyline, model(polyline))
plt.show()