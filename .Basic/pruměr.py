s=0
d=0

while True:
    c=int(input("Zadej čislo"))
    if c==0:
        break
    s+=c
    d+=1
    
print("pruměr je",s/d)