def funkcja(n):
    if n == 1:
        return 1
    if n == 2:
        return 5
    return funkcja(n - 1) - funkcja(n - 2)

print(funkcja(6))

