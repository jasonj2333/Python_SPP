kolory = ["czerwony", "zielony", "niebieski"]
kolory.append("pomarańczowy")
kolory.append("żółty")
kolory.insert(0, "biały")
kolory.insert(3, "czarny")

inne_kolory = ["różowy", "popielaty", "szary"]
kolory.extend(inne_kolory)
print(kolory)

kolory.remove("zielony")
kolory.pop()
kolory.pop(2)
#kolory.clear()
print(kolory)