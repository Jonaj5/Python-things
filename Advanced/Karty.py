from random import randint
pc=0
hrac=0

while hrac<=20:
    print("Maš ",hrac," bodů")
    odpoved=input("Chceš další kartu? - ")
    print("_____________________________")
    if odpoved=="ano" or odpoved=="jo" or odpoved=="jop" or odpoved=="yes" or odpoved=="jes" or odpoved=="ja" or odpoved=="da" or odpoved=="javol" or odpoved=="jistě" or odpoved=="samozřejmě" or odpoved=="si":
        karta=randint(2,10)
        hrac+=karta
        pc+=randint(2,10)
        
        if karta==10:
            print("Lízl jsis")
            print()
            print("╔══╗")
            print("║10║")
            print("╚══╝")
            print() 
        elif karta==9:
            print("Lízl jsis")
            print()
            print("┌─┐")
            print("│9│")
            print("└─┘")
            print()
        elif karta==8:
            print("Lízl jsis")
            print()
            print("┌─┐")
            print("│8│")
            print("└─┘")
            print()
        elif karta==7:
            print("Lízl jsis")
            print()
            print("┌─┐")
            print("│7│")
            print("└─┘")
            print()
        elif karta==6:
            print("Lízl jsis")
            print()
            print("┌─┐")
            print("│6│")
            print("└─┘")
            print()
        elif karta==5:
            print("Lízl jsis")
            print()
            print("┌─┐")
            print("│5│")
            print("└─┘")
            print()
        elif karta==4:
            print("Lízl jsis")
            print()
            print("┌─┐")
            print("│4│")
            print("└─┘")
            print()
            
        elif karta==3:
            print("Lízl jsis")
            print()
            print("┌─┐")
            print("│3│")
            print("└─┘")
            print()
        else:
            print("Lízl jsis")
            print()
            print("┌─┐")
            print("│2│")
            print("└─┘")
            print()
        
    else:
        break


print("_____________________________")
print(f"Maš ",hrac," bodů")
print(f"Počítač má ",pc," bodů")

if hrac==21:
    print("Vyhrál jsi")
elif pc==21:
    print("Počítač vyhrál")
elif hrac>=21:
    print("Prohrál jsi")
elif pc>=21:
    print("Počítač prohrál")
else:
    print("Remíza")