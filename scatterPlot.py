import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 8, 1, 10, 6])

plt.scatter(x, y)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Scatter Plot Example")

plt.show()