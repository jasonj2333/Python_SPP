import numpy as np
import matplotlib.pyplot as plt

partie = ["PiS", "KO", "Trzecia Droga", "Lewica", "Konfederacja", "BS", "PJJ"]
wyniki = [35.38, 30.70, 14.40, 8.61, 7.16, 1.86, 1.73]

#plt.title('Wybory parlamentarne 2023')
plt.subplot(211)
plt.bar(partie, wyniki)

plt.subplot(212)
plt.pie(wyniki, labels=partie, shadow=True, startangle=90)


plt.show()