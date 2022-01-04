def zad_a(s):
    w = ""
    for k in s:
        if k != 'm' and k != 'k':
            w += k
    return w 

def zad_b(s):
    j = 0
    for k in s:
        if k == 'a':
            j += 1
    return j

print("zad_a = ", zad_a("informatyka"))
print("zad_b = ", zad_b("informatyka"))

