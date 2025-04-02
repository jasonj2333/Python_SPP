tekst = "Ola ma kota Tolka, a kot Tolek ma Panią Olę"
dlugi_tekst = '''
Litwo! Ojczyzno moja! ty jesteś jak zdrowie.
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.
'''
szukany = "kot"

print(tekst)
print(dlugi_tekst)

print(tekst[0])
dl = len(tekst)
print(dl)
print(tekst[dl-1])
print(tekst[-3])
print(tekst[7:10])
print(tekst[4:-2])
print(tekst[4:-2:3])
print(tekst[9:])
print(tekst[:9])
print(tekst[::-1])

print(tekst.lower())
print(tekst.upper())
print(tekst.title())
print(szukany.capitalize())
print(szukany in tekst)
print(tekst.find(szukany))