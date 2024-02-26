import matplotlib.pyplot as plt

kwota_kredytu = 700000
liczba_rat = 360
oprocentowanie = 0.09

rata = kwota_kredytu * ((oprocentowanie/12) * (1 + (oprocentowanie/12))**liczba_rat) / ((1 + (oprocentowanie/12))**liczba_rat - 1)
#print(rata)

# K = kwota_kredytu
# p = oprocentowanie/12
# n = liczba_rat
# rata = K * (p*(1 + p)**n) / (((1 + p)**n) - 1 )
# print(rata)

tabela_rat = []
pozostala_kwota = kwota_kredytu
laczna_kwota = 0
tabela_kapitalowa = []
tabela_odsetkowa = []

for i in range(1, liczba_rat+1):
    odsetki = pozostala_kwota * oprocentowanie / 12
    czesc_kapitalowa = rata - odsetki
    pozostala_kwota -= czesc_kapitalowa
    tabela_rat.append((i, round(rata, 2), round(czesc_kapitalowa, 2), round(odsetki, 2), round(pozostala_kwota, 2)))
    

print("Nr raty | Wysokość raty | Część kapitałowa | Część odsetkowa | Pozostała kwota")
for numer, wysokosc_raty, czesc_kapitalowa, odsetki, pozostala_kwota in tabela_rat:
    print(f"{numer:>7} | {wysokosc_raty:>13} | {czesc_kapitalowa:>16} | {odsetki:>15} | {pozostala_kwota:>15}")
    laczna_kwota = laczna_kwota + czesc_kapitalowa + odsetki
    tabela_kapitalowa.append(czesc_kapitalowa)
    tabela_odsetkowa.append(odsetki)
    
print(f"Łączny koszt kredytu: {round(laczna_kwota, 2)}")

plt.plot(tabela_odsetkowa)
plt.plot(tabela_kapitalowa)
plt.title('Rata odsetkowa / kapitalowa')
plt.ylabel('Kwota w zł')
plt.xlabel('Okres spłaty w miesiącach')
plt.show()
