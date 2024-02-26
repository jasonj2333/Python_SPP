#import xlwt
import matplotlib.pyplot as plt

# kwota_kredytu = float(input("Podaj kwotę kredytu: "))
# liczba_rat = int(input("Podaj liczbę rat: "))
# oprocentowanie = float(input("Podaj oprocentowanie, np. jeśli wynosi 9%, zapisz 0.09: "))

kwota_kredytu = float(10000)
liczba_rat = 150
oprocentowanie = 0.09

rata = kwota_kredytu * ((oprocentowanie/12) * (1 + (oprocentowanie/12))**liczba_rat) / ((1 + (oprocentowanie/12))**liczba_rat - 1)
tabela_rat = []
pozostala_kwota = kwota_kredytu

for i in range(1, liczba_rat+1):
    odsetki = pozostala_kwota * oprocentowanie / 12
    czesc_kapitalowa = rata - odsetki
    pozostala_kwota -= czesc_kapitalowa
    tabela_rat.append((i, round(rata, 2), round(czesc_kapitalowa, 2), round(odsetki, 2), round(pozostala_kwota, 2)))
tabela_kapitalowa = []
tabela_odsetki = []

print("Nr raty | Wysokość raty | Część kapitałowa | Część odsetkowa | Pozostała kwota")
for numer, wysokosc_raty, czesc_kapitalowa, odsetki, pozostala_kwota in tabela_rat:
    tabela_kapitalowa.append(czesc_kapitalowa)
    tabela_odsetki.append(odsetki)
    print(f"{numer:>7} | {wysokosc_raty:>13} | {czesc_kapitalowa:>16} | {odsetki:>16} | {pozostala_kwota:>15}")

# plt.bar(tabela_numer, tabela_kapitalowa, color='r')
# plt.plot(tabela_odsetki)
# plt.title('Rata kapitałowa / odsetkowa')
# plt.ylabel('Wysokość spłaty (w zł)')
# plt.xlabel('Okres spłaty (w miesiącach)')
# plt.show()

# book = xlwt.Workbook(encoding="utf-8")
# sheet1 = book.add_sheet("Tabela rat")
# 
# sheet1.write(0, 0, "Nr raty")
# sheet1.write(0, 1, "Wysokość raty")
# sheet1.write(0, 2, "Część kapitałowa")
# sheet1.write(0, 3, "Część odsetkowa")
# sheet1.write(0, 4, "Pozostała kwota")
# 
# for row, (numer, wysokosc_raty, czesc_kapitalowa, odsetki, pozostala_kwota) in enumerate(tabela_rat, start=1):
#     sheet1.write(row, 0, numer)
#     sheet1.write(row, 1, wysokosc_raty)
#     sheet1.write(row, 2, czesc_kapitalowa)
#     sheet1.write(row, 3, odsetki)
#     sheet1.write(row, 4, pozostala_kwota)
# 
# book.save("tabela_rat.xls")
# print("Tabela rat została zapisana do pliku tabela_rat.xls.")