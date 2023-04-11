cislo1=float(input("Zadej první číslo"))
operace=input("Zadej operaci")
cislo2=float(input("Zadej druhé číslo"))

print(cislo1, operace, cislo2)
    
if operace == "+":
    print(cislo1 + cislo2)
elif operace == "-":
    print(cislo1 - cislo2)
elif operace == "*":
    print(cislo1 * cislo2)
elif operace == "/" and cislo2 == 0 or cislo1 == 0:
    print("Nelze dělit 0")
elif operace == "/":    
    print(cislo1 / cislo2)
elif operace == "**":
    print(cislo1 ** cislo2)
else :
    print("Špatná operace")