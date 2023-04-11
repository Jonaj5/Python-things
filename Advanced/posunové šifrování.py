zp=input("Zadej : ")
s=""

for zn in zp:
    x=ord(zn)
    
    if s=="x" or s=="y" or s=="z":
        a=chr(x-23)
        s+=a
    else:
        b=chr(x+3)
        s+=b
print(s)