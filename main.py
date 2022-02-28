import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

matplotlib.use('TkAgg')

x = np.linspace(0, 4*np.pi, 1000)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
fig.show()
