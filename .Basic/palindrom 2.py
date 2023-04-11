c=input("Zadej ").lower()
a=""
for z in c:
    if z in ".!?:; ,":
        a+=""
    else:
        a+=z
    
if a == a[::-1]:
    print("je palindrom")
else:
    print("není palindrom")
