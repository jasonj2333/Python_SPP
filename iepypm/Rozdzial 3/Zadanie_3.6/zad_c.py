# rekurencyjnie
def sklej(n):   
    if n == 1: return 0
    if n % 2 == 0: return n - 1 + 2 * sklej(n // 2)
    else: return n - 1 + sklej((n - 1) // 2) + sklej((n + 1) // 2)

# iteracyjnie
def zad_c(n):           
    s = [0 for row in range(n + 1)]
    for i in range(2, n + 1):
        if i % 2==0: s[i] = i - 1 + 2 * s[i // 2]
        else: s[i] = i - 1 + s[(i - 1) // 2] + s[(i + 1) // 2]   
    return s

print(sklej(10))
print(zad_c(10))










