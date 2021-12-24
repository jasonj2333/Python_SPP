def zad(WYPLATY):
    K = [200, 100, 50, 20, 10]
    LICZBY = [0, 0, 0, 0, 0]
    n = len(WYPLATY)
    for wyplata in WYPLATY:
         for j in range(5):
             LICZBY[j] += wyplata // K[j];
             wyplata %= K[j];
    return LICZBY

print(zad([130, 250, 310]))





