import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([3, 8, 1, 10])

plt.plot(x, y)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Plot with Grid")

plt.grid()   # add grid lines
plt.show()