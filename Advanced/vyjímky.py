while True:
    vstup=input("Zadej čislo : ")
    try:
        cislo=int(vstup)
        vysledek=1/cislo
    
    except ZeroDivisionError:
        print("Nelze dělit nulou")
    except ValueError:
        print("Neplatný znak")

    else:
        print(vysledek)
        break