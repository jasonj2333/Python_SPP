# Napisz prostą funkcję o nazwie stopnieFahrenheita(),
# funkcja dla podanych argumentu - stCelsjusz.
# np. stopnieFahrenheita(36),
# ma zwrócić wynik w stopniach Fahrenheita: 96.80.
# 
# Wzór na przeliczanie stopni znajdź w internecie.
# Wywołaj funkcje z argumentami 10, 20 stopnie Celsjusza.

def stopnieF(stopnieC):
    return stopnieC*9/5 + 32

sF = stopnieF(10)
print(sF)
sF = stopnieF(20)
print(sF)