#definicja funkcji
def hello():
    print("Cześć")

#Wywołanie funkcji
hello()
hello()

def uwaga(uczen, tresc="Korzystanie z telefon"):
    print(f"{uczen} otrzymuje uwagę za {tresc}")

uwaga("Patryk Bąbka", "Oglądanie YT")
uwaga("Sirous Illia", "Granie na lekcji")
uwaga("Sadowski Juliusz", "Korzystanie z telefonu")
uwaga("Eryk Holtzer")
