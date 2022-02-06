tekst = "matematyka"
wzorzec = "mat"

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

#metoda z wykorzystaniem find(tekst, start)
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


#print(znajdz_tekst(tekst, wzorzec, 0))
print(znajdz_wzorzec_find(tekst, wzorzec))