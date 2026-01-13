import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.title("Bar Chart")

plt.legend(["bar"])
plt.show()