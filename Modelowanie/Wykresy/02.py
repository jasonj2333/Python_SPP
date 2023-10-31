import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

y1 = [-2, -5, -7, -8, -3, 0, 2, 5, 4, 7, 11, 15]
y2 = [2, 5, 6, 4, 9, 11, 7, 8, 8, 11, 12, 10]
y3 = [-7, -5, 2, 0, 3, 6, 3, 1, 5, 3, 2, 2]

plt.plot(x, y1, 'bo-')
plt.plot(x, y2, 'g^--')
plt.plot(x, y3, 'r*-.')

plt.xticks(np.arange(0, 12+1, 1))
plt.title('Wykres pomiarów temperatury ze stacji S1, S2, S3')
plt.xlabel('Czas pomiaru [h]')
plt.ylabel('Temperatura [°C]')
plt.legend(["S1", "S2", "S3"], loc="best", fontsize="15")

plt.show()