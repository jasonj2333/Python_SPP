import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 1000)

y1 = x - 2
y2 = x ** 2 - 4

plt.plot(x, y1)
plt.plot(x, y2)

plt.axhline(0, color='black', linewidth=.5)
plt.axvline(0, color='black', linewidth=.5)

plt.axis((-10, 10, -10, 10))
plt.xticks(np.arange(-10, 10+1, 2))
plt.yticks(np.arange(-10, 10+1, 2))
plt.plot([2, -1], [0, -3], 'ro')

plt.show()