a=int(input("Zadej stranu A"))
b=int(input("Zadej stranu B"))

while a<0 or a==0:
    print("Neplatné číslo")
    a=int(input("Zadej stranu A"))

while b<0 or b==0:
    print("Neplatné číslo")
    b=int(input("Zadej stranu B"))
    
    
c=a*b

print("Obsah:")
print(c)