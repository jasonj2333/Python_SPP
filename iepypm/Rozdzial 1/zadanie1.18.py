def zad_a(s):
    j = 0
    for k in s:
        if k == 'd':
            j += 1
    return j

def zad_b(s):
    print(s[::-1])

def zad_c(s):
    j = 0
    for k in s:
        if k != 'a':
            j += 1
    return j

def zad_d(s):
    n = len(s)
    s = list(s)
    for i in range(n):
        if s[i] != 'b' and s[i] != 'B':
            s[i] = 'a'
    s = ''.join(s)        
    return s

def zad_e(s):
    w = ""
    for k in s:
        if k != 's':
            w += k
    return w   

def zad_f(s):
    n = len(s)
    k = 0
    for i in range(0, n, 3):
        if s[i] != 'd':
            k += 1
    return k

def zad_g(s):
    n = len(s)
    s = list(s)
    for i in range(n):
        if s[i] == 'm':
            s[i] = 'R'
    s = ''.join(s)        
    return s

print("zad_a = ", zad_a("subdominanta"))
zad_b("subdominanta")
print("zad_c = ", zad_c("subdominanta"))
print("zad_d = ", zad_d("subdominanta"))
print("zad_e = ", zad_e("subdominanta"))
print("zad_f = ", zad_f("subdominanta"))
print("zad_g = ", zad_g("subdominanta"))

