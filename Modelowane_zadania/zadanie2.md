# Zadanie 2 – Produkcja zestawów robotycznych

Firma produkuje trzy typy **zestawów robotycznych** dla szkół:

* **A** – zestaw podstawowy
* **B** – zestaw edukacyjny
* **C** – zestaw zaawansowany

Do produkcji wykorzystywane są trzy zasoby:

* czas pracy technika,
* liczba mikrokontrolerów,
* liczba czujników.

---

## Zużycie zasobów przez jeden zestaw

| Zestaw | Czas technika (h) | Mikrokontrolery | Czujniki |
| ------ | ----------------- | --------------- | -------- |
| A      | 1                 | 1               | 1        |
| B      | 2                 | 1               | 1        |
| C      | 1                 | 2               | 1        |

---

## Dostępne zasoby w magazynie

| Zasób           | Ilość |
| --------------- | ----- |
| Czas pracy      | 7 h   |
| Mikrokontrolery | 6     |
| Czujniki        | 5     |

---


# Model matematyczny

Z danych otrzymujemy układ:

x + 2y + z = 7 \
x + y + 2z = 6 \
x + y + z = 5


---

# Sprawdzenie w Pythonie

```python
import numpy as np


# ==========================
# Użyj następujących funkcji numpy
# ==========================

A = np.array([])

b = np.array([])

result = np.linalg.solve(A, b)

#Wyświetl rozwiazanie równania
```



