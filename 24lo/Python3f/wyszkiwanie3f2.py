tekst = "Bardzo lubię matematykę"
wzorzec = "mat"

def znajdz_wzorzec(tekst, szukany, start=0):
    dl1 = len(tekst)
    dl2 = len(szukany)
    
    for i in range(start, dl1-dl2+1):
        for j in range(dl2):
            if tekst[i+j] != szukany[j]:
                break
        if j == dl2-1:
            return i
    return -1

def znajdz_tekst(tekst, szukany):
    dl1 = len(tekst)
    dl2 = len(szukany)
    licznik = 0
    
    for i in range(dl1-dl2+1):
        if tekst[i] == szukany[0]:
            if tekst[i:i+dl2] == szukany:
                print(f"Znaleziono wzorzec {szukany} na pozycji {i}")
                licznik += 1
    if licznik == 0:
        print(f"Nie znaleziono wzorca {szukany} w tekście")
    else:
        print(f"Wzorzec znaleziono {licznik} razy")

print( znajdz_wzorzec( tekst, wzorzec, 18) )
znajdz_tekst(tekst, wzorzec)
print( tekst.find(wzorzec, 0) )