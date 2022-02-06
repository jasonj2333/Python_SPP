from random import randint
cenak = 1500
cenap = 200
w = randint(0, 25)
#w = 15
cenap_n = cenap * (1 + (w/100))

print(f'Cena komputera: {cenak} zł\t Cena płyty: {cenap} zł \t Zwrost ceny płyty: {w}% \t Nowa cena płyty głownej: {cenap_n}')

if w <= 10:
  print(f'Cena komputera wynosi {cenak} zł')
elif w > 20:
  print('Cena za wysoka')
else:
  cenak = (5/100)*cenap_n + cenak
  print(f'Cena komputera wynosi {cenak} zł')



# 1. Do zmiennej 'k' przypisz początkową cenę komputera
# 2. Do zmiennej 'cenap' przypisz początkową cenę płyty głównej
# 3. Do zmiennej 'w' przypisz wzrost ceny płyty głównej w %
# 4. Oblicz 'cenap_n = cenap + w%*cenap'
# 5. Jeżeli 'w <= 10' to wypisz 'k'
# 6. W przeciwnym razie Jeżeli 'w > 20' wypisz "za wysoka cena"
# 7. W przeciwnym razie wypisz 'k + 5%*cenap_n'