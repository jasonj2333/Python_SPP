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

tekst = "Bardzo lubie informatyke!"

def szyfr(tekst, tabela):
    tekst = tekst.upper()
    szyfrogram = ""
    
    for znak in tekst:
        if znak in tabela:
            szyfrogram += tabela[znak]
        else:
            szyfrogram += znak
    
    return szyfrogram

szyfrogram = szyfr(tekst, tabela_kodowania)
print(szyfrogram)
jawny = szyfr(szyfrogram, tabela_kodowania)
print(jawny)
