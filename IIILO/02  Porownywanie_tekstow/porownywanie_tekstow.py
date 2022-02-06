##### Algorytm porównywania tekstów i jego wykorzystanie do sprawdzenia sprawdzianu z angielskiego :)

## wersja podręcznikowa
def takie_same_while(t1, t2):
    i = 0
    dl1 = len(t1)
    dl2 = len(t2)
    while(i < dl1 and i < dl2 and t1[i] == t2[i]):
        i = i + 1
    return i == dl1 and i == dl2

#moja implementacja
def takie_same(tekst1, tekst2):
  tekst1, tekst2 = tekst1.lower(), tekst2.lower()
  if len(tekst1) != len(tekst2):
    return False

  for i in range(len(tekst1)):
    if tekst1[i] != tekst2[i]:
      return False
  
  return True

uczen = ["architekt", "scientist", "Biologist", "computer science", "nurse"] #lista odpowiedzi ucznia
wzor = ["architect", "scientist", "biologist", "computer scientist", "nurse"] #lista poprawnych odpowiedzi
punkty = 0

## sprawdzanie sprawdzianu
for i in range(len(uczen)):
  if(takie_same(uczen[i], wzor[i])):
    punkty += 1
    print(f"{uczen[i]} - dobrze ")
  else:
    print(f"{uczen[i]} - źle - poprawna forma {wzor[i]}")

print(f"Punkty: {punkty}")