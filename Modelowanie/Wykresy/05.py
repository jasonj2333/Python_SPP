import numpy as np
import matplotlib.pyplot as plt

costs = ['jedzenie', 'rozrywka', 'czynsz', 'odzież']
pln = [1356, 545, 1067, 220]

explode = [0, 0.2, 0, 0]

plt.pie(pln, labels=costs, shadow=True, startangle=90, explode=explode)

plt.show()