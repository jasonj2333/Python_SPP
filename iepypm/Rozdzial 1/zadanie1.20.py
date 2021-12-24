# sortowanie napisów metodą bąbelkową i przez wstawianie

def sortujbabelkowo(s):
    n = len(s)
    s = list(s)
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if s[i] > s[i + 1]:
                s[i], s[i + 1] = s[i + 1], s[i]
    s = ''.join(s)
    return s

def sortujprzezwstawianie(s):
    n = len(s)
    s = list(s)
    for i in range(1, n):
        pom = s[i]
        k = i - 1
        while k >= 0 and s[k] > pom:
            s[k + 1] = s[k]
            k -= 1
        s[k + 1] = pom
    s = ''.join(s)
    return s

print(sortujbabelkowo("9870345621"))
print(sortujprzezwstawianie("9870345621"))

