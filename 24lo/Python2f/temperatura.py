temperatury = [1.1, 3.9, 4, 7.7, 15.7, 20.4, 20.4, 20.9, 13.3, 11.4, 4.7, 0.7]
suma = 0

for sr_temp in temperatury:
    suma += sr_temp
    
srednia_roczna = suma / len(temperatury)
print(f"Średnia roczna temperatura wynosi: {srednia_roczna}")