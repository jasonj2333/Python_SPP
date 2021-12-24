def zad_c():
    x, y, z = 5, 1, 6    
    x += y
    if x > y + 1:
        x += z
        z -= 1
    if z < 3:
        z *= x
    else:
        z *= y
        z += 1 
    return x, y, z
    
print(zad_c())
