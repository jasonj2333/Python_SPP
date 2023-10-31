import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

def my_function(x):
    return x ** 3 + 2 * x - 6

plt.subplot(211)
plt.plot(x, my_function(x), 'g-')

plt.subplot(212)
parties = ['Ludzie', 'Elfy', 'Krasnoludy', 'Enty']
results = [21.56, 19.22, 28.12, 30.10]
plt.bar(parties, results)

plt.show()