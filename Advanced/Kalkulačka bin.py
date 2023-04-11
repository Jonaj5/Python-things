from definice import binar

operace = input("Zapiš operaci bin/dec - ")
cislo = input("Zapiš číslo - ")

if operace == "bin":
    cislo = int(cislo)
    print(binar(cislo))

else:
    
    vysledek2 = 0
    zbytek = len(cislo) - 1
    
    while zbytek != 0:
        bin.append(cislo[zbytek])
        zbytek = zbytek - 1
    
    bin.append(cislo[zbytek])
    zbytek = len(cislo) - 1
    
    while zbytek != 0:
        vysledek1 = 2 ** zbytek * int(bin[zbytek])
        zbytek = zbytek - 1
        vysledek1 = int(vysledek1)
        vysledek2 = vysledek1 + vysledek2
    
    vysledek1 = 2 ** zbytek * int(bin[zbytek])
    vysledek2 = vysledek1 + vysledek2
    
    print(vysledek2)