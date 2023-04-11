from random import randint
cislo = randint(1, 10)

print("Myslím si číslo od 1 do 10")
odhad = int(input("Jaké číslo si myslím?"))
while odhad != cislo:
    if odhad > cislo:
        odhad = int(input("Mé číslo je menší"))
    if odhad < cislo:
        odhad = int(input("Mé číslo je větší"))
if odhad == cislo:
    print("Uhádl jsi")