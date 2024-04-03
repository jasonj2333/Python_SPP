pkt = int(input("Podaj dotychczasową liczbę punktów: "))
f = float(input("Podaj frekwencje: "))
so = float(input("Podaj średnią: "))

if f > 94 and so >= 4.0:
    pkt += 20

print(f"Klasa zdobyła {pkt} punktów")
