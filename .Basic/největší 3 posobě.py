from random import randrange
from select import select
s=[]
while len(s)<31:
    s.append(randrange(1,11))
print(s)
max=0
for i in range(1,len(s)-1):
    if s[i]+s[i+1]+s[i+2]>max:
        max=s[i]+s[i+1]+s[i+2]
        
print(max)