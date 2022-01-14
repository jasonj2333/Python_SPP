miesiace = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]

suma_wplat = 0;

##### wersja dla listy miesięcy
for miesiac in miesiace:
    wplata = int(input("Wpłaty " + str(miesiac) + ": "))
    suma_wplat = suma_wplat + wplata

print("Suma wpłat wynosi: ", suma_wplat, " zł")