tekst = "matematyka"
wzorzec = "mat"

def znajdz_tekst(tekst, wzorzec, pozycja_startowa=0):
    dl1 = len(tekst)
    dl2 = len(wzorzec)
    
    for i in range(pozycja_startowa, dl1-dl2+1):
        for j in range(dl2):
            if tekst[i+j] != wzorzec[j]:
                break
        if j == dl2-1:
            return i
    return -1

print( znajdz_tekst(tekst, wzorzec, 0) )

def znajdz_wzorzec(tekst, wzorzec):
    dl1 = len(tekst)
    dl2 = len(wzorzec)
    liczba_wystapien = 0
    
    for i in range(dl1-dl2+1):
        if tekst[i] == wzorzec[0]:
            if tekst[i:i+dl2] == wzorzec:
                print(f"Znaleziono: {wzorzec} na pozycji {i}")
                liczba_wystapien += 1
    
    if liczba_wystapien == 0:
        print(f"Nie znaleziono wzorca: {wzorzec} w tekście {tekst}")
    else:
        print(f"Wzorzec znaleziono: {liczba_wystapien} razy")
        
znajdz_wzorzec(tekst, wzorzec)

print( tekst.find(wzorzec, 1) )
                
    