x=int(input("Zadej svůj věk"))
p=1
while x <1 or x >110:
    print("Špatně zadej znovu")
    x=int(input("Zadej svůj věk"))
    p+=1
if x<18 and x>0 :
    print("Nejsi dospělí")
else:
    print("Jsi dospělí")
print(p,"pokus")