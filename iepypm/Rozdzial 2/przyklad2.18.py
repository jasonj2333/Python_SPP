# znajdowanie anagramów przez sortowanie

def sortuj(s):
    n = len(s)
    s = list(s)
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if s[i] > s[i + 1]:
                s[i], s[i + 1] = s[i + 1], s[i]
    s = ''.join(s)
    return s

def anagramy():
    s1 = input("podaj pierwsze słowo: ")
    s2 = input("podaj drugie słowo: ")
    if len(s1) == len(s2):
        if sortuj(s1) == sortuj(s2):
            print("TAK")
        else:
            print("NIE")
    else:
        print("NIE")

anagramy()

