def znajdz_wzorzec(tekst, wzorzec):
  dl1 = len(tekst)
  dl2 = len(wzorzec)
  liczba_wystapien = 0

  for i in range(dl1-dl2+1):
    for j in range(dl2):
      if tekst[i+j] != wzorzec[j]:
        break
    else:
      print(f"Znaleziono: | {tekst} | {wzorzec} | {i}")
      liczba_wystapien += 1

  if liczba_wystapien == 0:
    print(f"Nie znaleziono wzorca: {wzorzec} w tekście {tekst}")
  else:
    print(f"Wzorzec: {wzorzec} występuję tekście {tekst}: {liczba_wystapien} razy")

znajdz_wzorzec("matematyka", "mat")