import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-10, 10, 1000)
y1 = x - 2

a = 1
b = 1
c = - 4
y2 = a* x ** 2 + b * x + c
delta = b**2 - 4*a*c

plt.axhline(0, color='black', linewidth=.5)
plt.axvline(0, color='black', linewidth=.5)
plt.xticks(np.arange(-10, 10+1, 2))
plt.yticks(np.arange(-10, 10+1, 2))
plt.axis((-10, 10, -10, 10))
#plt.plot(x, y1)
plt.plot(x, y2)

if(delta > 0):
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    plt.plot([x1], [0], 'ro')
    plt.plot([x2], [0], 'ro')
elif(delta == 0):
    x0 = -b / 2 * a
    plt.plot([x0], [0], 'ro')
    

plt.show()