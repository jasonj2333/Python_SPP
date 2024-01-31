import matplotlib.pyplot as plt
import numpy as np

#krowy
def C(t):
    return 30 * 2**t

#siano na krowę
def F(t):
    return 8 * 1.5**t

#siano do karmienia
def H(t):
    return C(t) * F(t)

lata = [0,2,4,6,8,10,12]
x = np.linspace(0, 12, 100)
siano = []
#print(H(t))
#print(240 * 3**t)
for rok in lata:
    print(f"Siano konieczne do karmienia {C(rok)} krów wynosi {H(rok):,.2f}")
    siano.append(H(rok))

plt.plot(x, H(x))
plt.show()

