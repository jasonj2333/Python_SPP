def zad_d():
    m, n, k = 5, 4, 0    
    if m + n < k:
        return k
    else:
        k = m + n
        if m + 1 < n:
            n *= 4
            k -= 1
        else:
            m *= 2
    return m, k, n
    
print(zad_d())
