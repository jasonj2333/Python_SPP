def zad(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while s[i] == ' ': i += 1
        while s[j] == ' ': j -= 1
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

if zad('może jutro ta dama sama da tortu jeżom'):
# if zad('zakopane na pokaz'):
    print("to jest palindrom")
else:
    print("to nie jest palindrom")


