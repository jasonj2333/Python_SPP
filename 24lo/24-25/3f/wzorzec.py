def znajdz_wzorzec(tekst, wzorzec):
    dl1 = len(tekst)
    dl2 = len(wzorzec)
    licznik = 0
    
    for i in range(dl1 - dl2 + 1):
        if tekst[i] == wzorzec[0]:
            if tekst[i:i+dl2] == wzorzec:
                print(f"Znaleziono: {wzorzec} na pozycji {i}")
                licznik += 1
    
    if licznik == 0:
        print("Nie znaleziono wzorca w tekście")
    else:
        print(f"Wzorzec znaleziono: {licznik} razy")
        
znajdz_wzorzec("matematyka", "mak")

tekst = "matematyka"
poz = tekst.find("mak", 1)
print(poz)
