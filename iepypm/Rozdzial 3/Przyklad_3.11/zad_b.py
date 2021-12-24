def zad_b(J, k):
    W = ''
    n = len(J)
    for j in range(k):
        i = j
        while i < n:
            W += J[i]
            i += k
    return W

print(zad_b('ZDAJĘ_MATURĘ_Z_INFORMATYKI',4))
print(zad_b('SPOTKANIE_WIECZOREM',3))
print(zad_b('POD_KINEM_EUROPA',5))
print(zad_b('O_GODZINIE_SIEDEMNASTEJ',5))






