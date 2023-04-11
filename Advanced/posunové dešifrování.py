zp=input("Zadej : ")
s=""
p=int(input("Posun o "))
print("")

for zn in zp:
    x=ord(zn)
    b=chr(x+p) 
    if x>ord("z"):
        b=chr(x-26)
        print(b)
        s+=b
    else:
        s+=b
print("Posun o",p)
print(s)
print("")

s=""
p+=1
ps=input("Posunout znovu? - ")
print("")

while True:
    if ps=="ano":
        for zn in zp:
            x=ord(zn)
            
            if x>ord("z"):
                a=chr(x-(26-p))
                s+=a
            else:
                b=chr(x+p)
                s+=b
                
        print("Posun o",p)
        print(s)
        print("")
        
        p+=1
        s=""
        ps=input("Posunout znovu? - ")
        print("")
    else:
        break