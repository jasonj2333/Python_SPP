names = ['John Johnson', 'Alicja Policja', 'Wladimir Wladymirowicz']

def get_sub_name(name, part=0):
    parts = name.split()
    return parts[part]

first_names = [get_sub_name(n, 0) for n in names]
print(first_names)

#last_names = [get_sub_name(n, 1) for n in names]
last_names =[(lambda n, p: n.split()[p])(name, 1) for name in names]
print(last_names)

last_names2 = [n.split()[1] for n in names]
print(last_names2)
