from itertools import combinations_with_replacement
import time

n = 9
start = 0
stop = 10**n-1

def armstrong_cm(start, stop):
    l = 0
    start_length = len(str(start)) if start != 0 else 0
    stop_length = len(str(stop))
    armstrongs_list = []
    for length in range(start_length, stop_length+1):
        found_numbers = []
        for digits in combinations_with_replacement(range(10), length):
            # make the digit power sum
            s = sum(d ** length for d in digits)

            # collect the digits of the sum
            temp = s
            sumdigits = []
            while temp:
                l+=1
                temp, d = divmod(temp, 10)
                sumdigits.append(d)

            # compare the two digit groups. Notice that "digits" is already sorted
            if list(digits) == sorted(sumdigits):
                found_numbers.append(s)

        # the sum-first-method doesn't find Armstrong numbers in order, so
        # an additional sorting is thrown in here.
        armstrongs_list.extend(sorted(found_numbers))

    armstrongs_list = [n for n in armstrongs_list if start <= n <= stop]
    print(l)
    return armstrongs_list

print(f"\n------- Wyszukiwanie liczb Armstronga w przedziale {start} - {stop:_} ----------------------")
start_time = time.time()

armstrongs = armstrong_cm(start, stop)

stop_time = time.time()
print(f"Znaleziono {len(armstrongs)} liczb(y) Armstronga: {armstrongs} ")
print(f"W czasie: {stop_time-start_time}")