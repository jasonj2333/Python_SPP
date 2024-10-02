# K01: i ← a ; obliczamy pierwszą liczbę parzystą
# K02: Jeśli a mod 2 ≠ 0, 
#      to i ← i+1
# K03: Dopóki i ≤ b: ; generujemy liczby parzyste w przedziale <a, b>
#      wykonuj kroki K04…K05
# K04:   Pisz i ; wyprowadzamy liczbę parzystą
# K05:   i ← i+2 ; następna liczba parzysta
# K06: Zakończ

def parzyste(a, b):
    i = a
    if a % 2 != 0:
        i += 1
    while i <= b:
        print(i, end=" ")
        i += 2

parzyste(4, 28)
print()
parzyste(-7, 33)
print()
nieparzyste(-7, 33)
