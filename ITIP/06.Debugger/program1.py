x = float(input("Podaj liczbę x: "))
y = float(input("Podaj liczbę y: "))


def pierwsza_funkcja(x, y):
    z = 5
    x = x + 2
    if x < y:
        x = x * z
        y = y - 1
        return x, y
    else:
        if x == y:
            y = y - z
            x = x - 1
            return x, y
        else:
            y = y + z
            x = x + 1
            return x, y

def druga_funkcja():
    a = 3
    b = -2
    c = 10
    if a+b < c:
        a *= 2
        b -= 1
        if c > 0:
            c += a
            return a, b, c
        else:
            c += b
            return a, b, c
    else:
        c += a*b
        return a, b, c


x, y = pierwsza_funkcja(x, y)

print(f"x to: {x} a y to: {y}")

a, b, c = druga_funkcja()
print(a, b, c)