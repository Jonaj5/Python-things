text=input("zadej text")
pocet=len(text)-1
s=0
while pocet!=0:
    if text[pocet] in "aáeéiíouúůyý":
        s+=1
    pocet-=1
if text[pocet] in "aáeéiíouúůyý":
        s+=1
print(s)