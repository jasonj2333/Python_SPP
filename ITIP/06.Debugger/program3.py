#Algorytm 1.4 - patrz zadanie.jpg
# 1. Wczytaj zmienne a = 3, b= - 2, c= 10
# 2. Jeżeli a + b < c przejdź do kroku 3 w przeciwnym razie do kroku 6
# 3. a *+2, b-=1
# 4. Jeżeli c > 0 to c+=a w przeciwnym razie c += b
# 5. Przejdź do kroku 7
# 6. c +=a*b
# 7. Wypisz a, b, c

#Program działa i dla poniższych danych daje poprawne wyniki,
#ale nie jest to poprawnie napisany program, bo dla innych danych
#wejściowych, może dać błędne rezultaty

a = 3
b = -2
c = 10

if a + b < c:
    a*= 2
    b-= 1
else: c+= a * b

if c > 0:
  c+= a
else:
  c+= b
print("a=", a)
print("b=", b)
print("c=", c)