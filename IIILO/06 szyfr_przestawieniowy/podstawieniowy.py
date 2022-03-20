tabela_kodowania = {
    "A":"Z",
    "B":"Y",
    "C":"X",
    "D":"W",
    "E":"V",
    "F":"U",
    "G":"T",
    "H":"S",
    "I":"R",
    "J":"Q",
    "K":"P",
    "L":"O",
    "M":"N",
    "N":"M",
    "O":"L",
    "P":"K",
    "Q":"J",
    "R":"I",
    "S":"H",
    "T":"G",
    "U":"F",
    "V":"E",
    "W":"D",
    "X":"C",
    "Y":"B",
    "Z":"A",
}

def koduj(tekst, tabela_kodowania):
    tekst = tekst.upper()
    szyfrogram = ''
    
    for znak in tekst:
        if znak in tabela_kodowania:
            szyfrogram += tabela_kodowania[znak]
        else:
            szyfrogram = znak
            
    return szyfrogram

print(koduj('informatyka', tabela_kodowania))