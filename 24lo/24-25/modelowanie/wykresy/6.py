import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
k = 1
m = -2
a = 3
b = 2
c =  -4

y1 = k*x + m
y2 = a*(x ** 2) + b*x + c

D = b**2 - 4*a*c
x01 = (-b + D ** 0.5) / (2*a)
x02 = (-b - D ** 0.5) / (2*a)

plt.plot(x, y1)
plt.plot(x, y2)

plt.plot(x01, 0, 'ro')
plt.plot(x02, 0, 'ro')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.axis( (-10, 10, -10, 10) )
plt.show()