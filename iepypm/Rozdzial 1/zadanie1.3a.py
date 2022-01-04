def zad_a(x, y):
    z = 5
    x += 2
    if x < y:
        x *= z
        y -= 1
    elif x == y:
        y -= z
        x -= 1
    else:
        y += z
        x += 1
    return x, y
    
print(zad_a(-3, 4))
