def zad_a(s):
    n = len(s)
    print("zad_a")
    for i in range(n):
        if s[i] != 'm' and s[i] != 'k':
            print(s[i])

def zad_b(s):
    n = len(s)
    j = 0
    for i in range(n):
        if s[i] == 'a':
            j += 1
    return j

def zad_c(s):
    n = len(s)
    k = 0
    for i in range(0, n, 2):
        if s[i] != 'f':
            k += 1
    return k

def zad_d(s):
    n = len(s)
    s = list(s)
    for i in range(n):
        if s[i] == 'o':
            s[i] = 'x'
    s = ''.join(s)       
    return s

def zad_e(s):
    n = len(s)
    s = list(s)
    for i in range(n):
        if s[i] != 'm' and s[i] != 'a':
            s[i] = 'W'
    s=''.join(s)        
    return s
           
zad_a("informatyka")
print("zad_b = ", zad_b("informatyka"))
print("zad_c = ", zad_c("informatyka"))
print("zad_d = ", zad_d("informatyka"))
print("zad_e = ", zad_e("informatyka"))

