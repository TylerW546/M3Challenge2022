import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import scipy

from AvailableRemoteWorkers import *

# Exponential function
def exponential(x, a, b, c):
    return a * np.exp(-b * x) + c


fullyHomeDatePre  = []
fullyHomePre = []
partialHomeDatePre = []
partialHomePre = []

# Parse through pre covid partial and fully online rates
with open('D4-Inputs/Pre-Covid.txt') as f:
    lines = f.readline().split()
    while lines:
        print(lines)
        fullyHomeDatePre.append(int(lines[0]))
        fullyHomePre.append(float(lines[1][0 : len(lines[1])-2]))
        if lines[2] != '-':
            partialHomePre.append(float(lines[2][0 : len(lines[2])-2]))   
            partialHomeDatePre.append(int(lines[0]))

        lines = f.readline().split()
f.close()


fullyHomeDatePost  = []
fullyHomePost = []
partialHomeDatePost = []
partialHomePost = []

# Parse through post covid partial and fully online rates
with open('D4-Inputs/Post-Covid.txt') as f:
    lines = f.readline().split()
    while lines:
        print(lines)
        fullyHomeDatePost.append(((int(lines[0][0:2])/12) + (int(lines[0][3:]))))
        fullyHomePost.append(float(lines[1][0 : len(lines[1])-2]))
        if lines[2] != '-':
            partialHomePost.append(float(lines[2][0 : len(lines[2])-2]))   
            partialHomeDatePost.append((int(lines[0][0:2])/12) + (int(lines[0][3:])))

        lines = f.readline().split()
f.close()

print(len(fullyHomeDatePost))
print(len(fullyHomePost))






# Set up of graph
polyline = np.linspace(2000, 2030, 50)


# Plot Pre covid rates in scatter plot then create regression

#polynomial fit with degree = 2
fullHomeModelPre = np.poly1d(np.polyfit(fullyHomeDatePre, fullyHomePre, 2))
partialHomeModelPre = np.poly1d(np.polyfit(partialHomeDatePre, partialHomePre, 1))




# subtract the pre-covid fully at home prediction from pos-covid fully at home predriction data for use in regression
for i in range(len(fullyHomePost)):
    fullyHomePost[i] = max(fullyHomePost[i] - fullHomeModelPre(fullyHomeDatePost[i]), 0)

# Transform post-covid partially at home data prediction to be used in a binomial regression
print(partialHomePost)
for i in range(len(partialHomeDatePost)):
    partialHomePost[i] = np.log((partialHomeModelPre(partialHomeDatePost[i])/partialHomePost[i]) - 1)
print(partialHomePost)

# Regress partial and full working from home after logging each
fullHomeModelPost = np.poly1d(np.polyfit(fullyHomeDatePost, np.log(fullyHomePost), 1))
partialHomeModelPost = np.poly1d(np.polyfit(partialHomeDatePost, partialHomePost, 1))

for i in range(len(partialHomeDatePost)):
    print(partialHomeModelPost(partialHomeDatePost[i]), end=', ')
    # print(partialHomeModelPre(partialHomeDatePost[i]) / (1 + np.e**partialHomeModelPost(partialHomeDatePost[i])), end=', ')



def plotPercentages():
    
    plt.ylim(0, 60)
    plt.title('The Percentage of People Working Fully and Partially at Home')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    
    # Plot scatter plots of full and partial working from home
    plt.scatter(fullyHomeDatePre, fullyHomePre, label='Pre-Covid Fully At Home: DATA')
    plt.scatter(partialHomeDatePre, partialHomePre, label='Pre-Covid Partial At Home: DATA')


    # Plot regressions of full and partial working from home data
    plt.plot(polyline, fullHomeModelPre(polyline), label='Pre-Covid Fully At Home: REGRESSION')
    plt.plot(polyline, partialHomeModelPre(polyline), label='Pre-Covid Partial At Home: REGRESSION')

    # graph total percentage of people working at home in any capacity before start of covid
    plt.plot(polyline, fullHomeModelPre(polyline) + partialHomeModelPre(polyline), label='Pre-Covid Working at Home Total')



    # Plot post covid rates in scatter plot then create regression


    # Plot scatter plots of full and partial working from home
    plt.scatter(fullyHomeDatePost, fullyHomePost, label='Post-Covid Fully At Home: DATA')
    plt.scatter(partialHomeDatePost, partialHomePost, label='Post-Covid Partial At Home: DATA')


    # Reverse transforms made before regressing then plot the functions projecting fully and partially at home
    plt.plot(polyline, np.e**fullHomeModelPost(polyline)+fullHomeModelPre(polyline), label='Post-Covid Fully At Home: REGRESSION')
    plt.plot(polyline, partialHomeModelPre(polyline) / (1 + np.e**partialHomeModelPost(polyline)), label='Post-Covid Partial At Home: REGRESSION')

    # graph total percentage of people working at home in any capacity after start of covid
    plt.plot(polyline, np.e**fullHomeModelPost(polyline)+fullHomeModelPre(polyline) + partialHomeModelPre(polyline) / (1 + np.e**partialHomeModelPost(polyline)), label='Post-Covid Working at Home Total')



y = []
for i in range(2000,2030):
    # All workers * Remote Workers
    y.append(globalWorkersList[i-2000]*(np.e**fullHomeModelPost(i)+fullHomeModelPre(i) + partialHomeModelPre(i) / (1 + np.e**partialHomeModelPost(i)))/100)

def plotRemoteWorkers():
    plt.plot([i for i in range(2000,2030)], y, label="True Remote Workers")
    
plt.ylim(0, 60000000)

plotAverageRemoteWorkers()
plotRemoteWorkers()

y2 = []
for val in y:
      pass


# Display Plot
plt.legend(loc='upper left')
plt.show()