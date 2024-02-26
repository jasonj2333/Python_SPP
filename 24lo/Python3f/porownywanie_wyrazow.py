tekst1 = "Informatyka"
tekst2 = "informatyka"

def takie_same(t1, t2):
    i = 0
    dl1 = len(t1)
    dl2 = len(t2)
    
    while(i < dl1 and i < dl2 and t1[i] == t2[i]):
        i += 1
    return i == dl1 and i == dl2

print( takie_same(tekst1, tekst2) )

def identyczne(t1, t2):
    t1, t2 = t1.lower(), t2.lower()
    if len(t1) != len(t2):
        return False
    
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            return False
    return True

print( identyczne(tekst1, tekst2) )

uczen = ["architekt", "scientist", "Biologist", "computer science", "nurse"] #lista odpowiedzi ucznia
wzor = ["architect", "scientist", "biologist", "computer scientist", "nurse"] #lista poprawnych odpowiedzi
punkty = 0

#sprawdzanie kartkówki
for odp in range(len(uczen)):
    if takie_same(uczen[odp], wzor[odp]):
        punkty += 1
        print(f"{uczen[i]} - dobrze")
    else:
        print(f"{uczen[i]} - źle - poprawna forma {wzor[i]}")