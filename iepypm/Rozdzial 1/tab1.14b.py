# zapisywanie napisów do pliku
zapis=open("wyniki1.14a.txt", "w")
zapis.write("wiersz1\n")
zapis.write("wiersz2\n")
zapis.write("wiersz3\n")
zapis.close()

# zapisywanie listy napisów do pliku
zapis=open("wyniki1.14b.txt", "w")
lista=["wiersz1\n", "wiersz2\n", "wiersz3\n"]
zapis.writelines(lista)
zapis.close()

