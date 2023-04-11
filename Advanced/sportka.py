from random import randrange

n=0
o=[]
i=0

while i !=6:
    n=randrange(0,50)
    if n not in o:
        o.append(n)
        i+=1
print(o)




    

