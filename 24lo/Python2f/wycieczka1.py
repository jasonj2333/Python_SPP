# Utwórz listę wycieczka na której umieść imiona:
#     - Ala, Wojtek
# Dopisz do listy na końcu:
#     - Grześka, Olę, Tomka
# Dodaj do listy na początku:
#     - Ewę
# Usuń z listy:
#     - Olę
#     - ostatnią osobę na liście
# Wyświetl uczestników wycieczki w formie listy
wycieczka = ["Ala", "Wojtek"]
wycieczka.append("Grzesiek")
wycieczka.append("Ola")
wycieczka.append("Tomek")
wycieczka.insert(0, "Ewa")
wycieczka.remove("Ola")
wycieczka.pop()
wycieczka.sort()

for imie in wycieczka:
    print(imie)

