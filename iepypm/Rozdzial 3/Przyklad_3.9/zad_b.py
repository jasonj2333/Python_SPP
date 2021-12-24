def zad_b(s):
    w = 0
    k = 0.25
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ',':
            w += k*(ord(s[i]) - ord('0'))
            k *= 2
    return w

print(zad_b('100,01'))





