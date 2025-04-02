def porownaj(tekst1, tekst2):
    tekst1, tekst2 = tekst1.lower(), tekst2.lower()
    if len(tekst1) != len(tekst2):
        return False
    
    for i in range(len(tekst1)):
        if tekst1[i] != tekst2[i]:
            return False
    return True

print( porownaj("Matematyka", "matematyka") )
print( porownaj("poniedziałek", "po niedzieli") )

if porownaj("Matematyka", "matematyka"):
    print("Wyrazy są takie same")
else:
    print("Wyrazy nie są takie same")