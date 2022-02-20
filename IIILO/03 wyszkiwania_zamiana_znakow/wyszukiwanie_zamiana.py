tekst = "matematyka"
szukany_znak = "a"
nowy_znak = "X"

def zlicz_znaki(tekst, szukany_znak):
  liczba_znakow = 0
  
  for znak in tekst:
    if znak == szukany_znak:
      liczba_znakow += 1
  
  return liczba_znakow

def zamien_znaki(tekst, szukany_znak, nowy_znak):
  nowy_tekst = ''
  for znak in tekst:
    if znak == szukany_znak:
      znak = nowy_znak
    nowy_tekst += znak
  return nowy_tekst

#wersja count()
print(f"Liczba znaków '{szukany_znak}' w tekście '{tekst}' wynosi {tekst.count(szukany_znak)}")  

#iteracyjnie
print(f"Liczba znaków '{szukany_znak}' w tekście '{tekst}' wynosi {zlicz_znaki(tekst, szukany_znak)}")

#zamiana znaków
print(f"Tekście '{tekst}' zamieniam '{szukany_znak}' na {nowy_znak} nowy tekst {zamien_znaki(tekst, szukany_znak, nowy_znak)}")
