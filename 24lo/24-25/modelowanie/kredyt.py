import matplotlib.pyplot as plt

kwota_kredytu = 500000
liczba_rat = 360
oprocentowanie = 0.09
# K - kwota kredytu
# p = oprocentowanie
# n = liczba rat
#rata = K * (p*(1 + p)**n) / (((1 + p)**n)-1)
rata = kwota_kredytu * ((oprocentowanie/12) * (1 + (oprocentowanie/12))**liczba_rat) / (((1 + (oprocentowanie/12))**liczba_rat) - 1)
#print(rata)

tabela_rat = []
pozostala_kwota = kwota_kredytu
laczna_kwota = 0
tabela_kapitalowa = []
tabela_odsetkowa = []
tabela_numer = []

for i in range(1, liczba_rat+1):
    odsetki = pozostala_kwota * (oprocentowanie / 12)
    czesc_kapitalowa = rata - odsetki
    pozostala_kwota -= czesc_kapitalowa
    tabela_rat.append( (i, round(rata, 2), round(czesc_kapitalowa,2), round(odsetki, 2), round(pozostala_kwota, 2) ))
    

print("Nr raty | Wysokość raty | Cześć kapitałowa | Cześć odsetkowa | Pozostała kwota")
for numer, wysokosc_raty, czesc_kapitalowa, odsetki, pozostala in tabela_rat:
    print(f"{numer:>7} | {wysokosc_raty:>13} | {czesc_kapitalowa:>16} | {odsetki:>15} | {pozostala:>15}")
    laczna_kwota = laczna_kwota + czesc_kapitalowa + odsetki
    tabela_kapitalowa.append(czesc_kapitalowa)
    tabela_odsetkowa.append(odsetki)
    tabela_numer.append(numer)
    
print(f"Łączny koszt kredytu: {laczna_kwota}")

plt.bar(tabela_numer, tabela_kapitalowa, color="r")
plt.plot(tabela_odsetkowa)
plt.title("Rata kapitałowa / odsetkowa")
plt.ylabel("Wysokość raty (zł)")
plt.xlabel("Okres spłaty (w miesiącach)")
plt.show()
    
    
    
    
    