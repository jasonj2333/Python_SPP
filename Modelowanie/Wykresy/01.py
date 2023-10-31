import numpy as np
import matplotlib.pyplot as plt

plt.plot([5],[7], 'ro')
plt.plot([12],[4], 'b^')

plt.axis((0, 15, 0, 10))

plt.xticks(np.arange(0, 15+1, 1))
plt.yticks(np.arange(0, 10+1, 1))

plt.show()