o1 = int( input("Podaj liczbę osób uwzględnionych w przepisie: ") )
o2 = int( input("Podaj liczbę osób na spotkaniu: ") )
s1 = float( input("Podaj ilość składnika z przepisu: ") )

s2 = s1 * o2 / o1

print(f"Dla {o2} osób potrzeba {s2:.2f} składnika sałatki")