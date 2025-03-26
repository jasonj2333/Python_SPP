import time

max_limit = 50000

my_list = list(range(max_limit))
my_set = set(range(max_limit))

# checking time for list search

start = time.time()

for p in range(max_limit):
   is_present = p in my_list

stop = time.time()

print(f'List search operation duration was {stop - start}')

# checking time for set search

start = time.time()

for p in range(max_limit):
   is_present = p in my_set

stop = time.time()

print(f'Set search operation duration was {stop - start}')