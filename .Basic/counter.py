
v=input("Zadej větu")
p=0
c=0
o=0
for i in v:
    if i.isalpha():
        p+=1
    elif i.isdigit():
        c+=1
    else:
        o+=1

print(p," - pismen")
print(c," - čisel")
print("zbytek - ",o)