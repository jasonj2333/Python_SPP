# Napisz funkcję o nazwie poleKola(),
# funkcja dla podanego promienia: np. poleKola(1),
# ma wypisać na stronie tekst:
#     Pole koła o promieniu: 1 wynosi: 3.141592653589793.
# 
# Wywołaj funkcję z argumentami 1,2,10.

import math

def poleKola(promien):
    pole = math.pi * promien * promien
    print(f"Pole koła o promieniu {promien} wynosi: {pole}")
    
poleKola(1)
poleKola(2)
poleKola(10)