while True:
    vstup=input("Zadej čislo 1-10 : ")
    try:
        cislo=int(vstup)
        if cislo<1 or cislo>10:
            raise ValueError
    except ValueError:
        print("Neplatný znak")

    else:
        print(f"Zadal jsi {cislo}")
        break