import math

def je_prvocislo(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def součin(*cisla):
    vysledek = 1
    for cislo in cisla:
        vysledek *= cislo
    return vysledek

def učetnictví(zustatek, *polozky, urok=0.0):
    vystup = zustatek
    for polozka in polozky:
        vystup += polozka
    vystup *= (1 + urok / 100)
    return vystup

def binar(cislo):
    bin = []
    while cislo != 0:
        cislo, zbytek = divmod(cislo, 2)
        bin.append(zbytek)
    bin = bin[::-1]
    return bin

def decimal(cislo):
    input = str(cislo)
    vysledek = 0
    zbytek = len(input) - 1
    while zbytek >= 0:
        vysledek += int(input[zbytek]) * 2 ** zbytek
        zbytek -= 1
    return vysledek

def součet(zaklad, *cisla):
    vysledek = zaklad
    for cislo in cisla:
        vysledek += cislo
    return vysledek

def mocnina(zaklad, exponent=2):
    return pow(zaklad, exponent)

