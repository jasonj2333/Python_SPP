def zad(x, n):
    if n == 0:
        return 1
    return zad(x, n - 1) * x

print(zad(2, 3))
print(zad(3, 4))

