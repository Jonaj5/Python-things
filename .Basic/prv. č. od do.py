from definice import je_prvocislo
v=int(input("Dolní číslo"))
a=int(input("Horní číslo"))
p=[]

for i in range(v, a+1):
    if je_prvocislo(i):p.append(i)
print(p)
    
        
    


    