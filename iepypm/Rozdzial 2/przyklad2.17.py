# sortowanie tekstu metodą przez wybór

def sortujprzezwybor(s):
    n = len(s)
    s = list(s)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if s[j] < s[k]:
                k = j
        s[k], s[i] = s[i], s[k]
    s = ''.join(s)
    return s

print(sortujprzezwybor("zxcvbnmas"))


