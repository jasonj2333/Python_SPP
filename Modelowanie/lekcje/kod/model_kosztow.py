# Sytuacja: firma kurierska nalicza opłatę:
# 5 zł opłata startowa + 2 zł za każdy km.
# 
# y = 2x + 5
# a - opłata za km
# b - opłata startowa

def koszt_przesylki(km, a=2, b=5):
    return a*km + b

przesylki = [6, 12, 7, 18, 90]
koszt = []

for p in przesylki:
    print(f"Koszt przesyłki wysłanej na odległość: {p} km wynosi {koszt_przesylki(p)}")
    koszt.append(koszt_przesylki(p))
    
import matplotlib.pyplot as plt
plt.plot(przesylki, koszt)
plt.show()