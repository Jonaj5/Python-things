bin=[]
cislo1=input("Zadej první číslo")
cislo2=0

operace=input("Zadej operaci")
if operace == "dec" or operace == "bin":
    print(f"cislo1 do operace")
    
else :
    cislo2=float(input("Zadej druhé číslo"))
    print(cislo1, operace, cislo2)
    
    
if operace == "+":
    cislo1=float(cislo1)
    print(cislo1 + cislo2)

elif operace == "-":
    cislo1=float(cislo1)
    print(cislo1 - cislo2)

elif operace == "*":
    cislo1=float(cislo1)
    print(cislo1 * cislo2)

elif operace == "/":
    cislo1=float(cislo1)
    if operace == "/" and cislo1 == 0 or cislo2 == 0:
        print("Nelze dělit 0")
    else:
        print(cislo1 / cislo2)

elif operace == "**":
    cislo1=float(cislo1)
    print(cislo1 ** cislo2)

elif operace == "bin":
    int(cislo1)
    
    while cislo1 != 0:
        zbytek = cislo1 % 2
        cislo1 = (cislo1 - zbytek) / 2
        bin.append(zbytek)
    vysledek = len(bin) - 1
    
    while vysledek != 0:
        print(bin[vysledek])
        vysledek = vysledek - 1
    print(bin[0])

elif operace == "dec":
    
    vysledek2 = 0
    zbytek = len(cislo1) - 1
    
    while zbytek != 0:
        bin.append(cislo1[zbytek])
        zbytek = zbytek - 1
    
    bin.append(cislo1[zbytek])
    zbytek = len(cislo1) - 1
    
    while zbytek != 0:
        vysledek1 = 2 ** zbytek * int(bin[zbytek])
        zbytek = zbytek - 1
        vysledek1 = int(vysledek1)
        vysledek2 = vysledek1 + vysledek2
    
    vysledek1 = 2 ** zbytek * int(bin[zbytek])
    vysledek2 = vysledek1 + vysledek2
    
    print(vysledek2)
else :
    print("Špatná operace")