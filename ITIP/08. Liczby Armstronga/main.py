import time

# Liczby Armstronga

start = 0
stop = 100_000_000

#funkcja obliczająca sumę n-potęg cyfr danej liczby
def get_sum(number, n):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit ** n
        number //= 10

    return sum

#wersja klasyczna
def armstrong(number):
    # ilosc cyfr
    n = len(str(number))
    
    sum = get_sum(number, n)
    

    if number == sum: return True
    
    return False


# szybsza metoda
def armstrong10(number):
    #ilość cyfr
    n = len(str(number))
    
    sum = 0
    temp = number//10
    
    #oblicza sumę n-potęg podanej liczby np: 150 sum = 126
    sum = get_sum(temp, n)

    #do obliczonej sumy dodajemy n - potęgi cyfr w rzędzie jedności od 0 do 9
    for i in range(0, 10):
        #jeżeli jest to liczba Armstronga to wyświetlamy w konsoli
        result = sum + i ** n
        if  result == number + i:
            print(result)

#założenie - jako argument dla funkcji armstrong podajemy liczbę - musi mieć na końcu zero np. 150
start_time = time.time()

#metoda szybka
for number in range(start, stop + 1, 10):
    armstrong10(number)

#metoda klasyczna
# for number in range(start, stop + 1):
#     if armstrong(number):
#         print(number)

print(f"--- {time.time() - start_time} seconds ---")

#### Na wyszukanie liczb Armstronga w przedziale 0 do 1 000 000 000 mój komputer potrzebował --- 667.2648086547852 seconds ---
#### znalezione w tym czasie liczby to:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 153
# 370
# 371
# 407
# 1634
# 8208
# 9474
# 54748
# 92727
# 93084
# 548834
# 1741725
# 4210818
# 9800817
# 9926315
# 24678050
# 24678051
# 88593477
# 146511208
# 472335975
# 534494836
# 912985153

#Łącznie 32