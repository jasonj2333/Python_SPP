koszt_komputera = 4000
konto = 0

for i in range(12):
    wplata = int( input('Ile wpłacasz: ') )
    konto = konto + wplata

print('Zebrałeś', konto, 'zł')
print('Komputer kosztuje', koszt_komputera, 'zł')

if konto - koszt_komputera >= 0:
    print('Brawo, możesz kupić komputer.')
else:
    print('Nie udało ci się zebrać wymaganej kwoty.')
    print('Brakuje ci jeszcze:', koszt_komputera - konto)