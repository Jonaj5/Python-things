bin=[]
pismena=0
x=input("Zadej slovo")
zbytek = len(x) - 1
y=int(input(f"Zadej číslo 0 - {zbytek}"))

while y>zbytek :
    y=int(input(f"Moc vysoké číslo zadej 0 - {zbytek}"))
print(zbytek)

while zbytek != pismena :
    print(bin)
    bin.append(x[pismena])
    pismena=pismena+1
    print(pismena)
print(bin)