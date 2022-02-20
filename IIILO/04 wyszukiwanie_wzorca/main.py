tekst = "matematyka"
wzorzec = "mat"

#wersja z podręcznika - funkcja zwracająca pierwsze (od pozycji startowej) wystąpienie wzorca - pozycje 1 litery wzorca
#lub -1 gdy wzorzec nie występuje
def znajdz_tekst(tekst, wzorzec, pozycja_startowa):
  dl1 = len(tekst)
  dl2 = len(wzorzec)

  for i in range(pozycja_startowa, dl1-dl2+1):
    for j in range(dl2):
      if tekst[i+j] != wzorzec[j]:
        break
    if j == dl2-1:
      return i
  return -1

#moja wersja z funkcją nie zwracającą wartości, tylko wypisującą wystąpienia wzorca
def znajdz_wzorzec(tekst, wzorzec):
  dl1 = len(tekst)
  dl2 = len(wzorzec)
  liczba_wystapien = 0

  for i in range(dl1-dl2+1):
    if tekst[i] == wzorzec[0]:
      if tekst[i:i+dl2] == wzorzec:
        print(f"Znaleziono: | {tekst} | {wzorzec} | {i}")
        liczba_wystapien += 1
  
  if liczba_wystapien == 0:
      print(f"Nie znaleziono wzorca: {wzorzec} w tekście {tekst}")
  else:
      print(f"Wzorzec znaleziono: {liczba_wystapien} razy")

#metoda z wykorzystaniem find(tekst, start) - metoda zwracająca pierwsze wystąpienie wzorca (od pozycji startowej)
# lub -1 gdy wzorzec nie występuje
# Funkcja zwraca wszystkie wystąpienia wzorca w formie listy na podstawie której można wypisać wystąpienia ich liczbę
def znajdz_wzorzec_find(tekst, wzorzec):
  dl1 = len(tekst)
  dl2 = len(wzorzec)
  wystapienia = []
  poz = 0
  while poz < dl1-dl2+1 and poz != -1:
    poz = tekst.find(wzorzec, poz)
    if poz !=-1: 
      wystapienia.append(poz)
      poz += 1
  return wystapienia

## Przykładowe użycie
print(znajdz_tekst(tekst, wzorzec, 0))
znajdz_wzorzec(tekst, wzorzec)
print(znajdz_wzorzec_find(tekst, wzorzec))