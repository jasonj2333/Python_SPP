my_list = list(range(10))

def fun_square(x):
    return x*x

#new_list = [fun_square(x) for x in my_list]
#new_list = [x*x for x in my_list]

#funkcja lambda
new_list = [(lambda x: x*x)(x) for x in my_list]
new_list = [x*x for x in my_list]

print(new_list)