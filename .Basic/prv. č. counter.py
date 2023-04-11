cislo=int(input("zadej cislo"))
pocet=0
for i in range(0,cislo+1):
    zbytek1=i%2
    zbytek2=i%3
    zbytek3=i%5
    zbytek4=i%7
    if zbytek1 >= 1 and zbytek2 >= 1 and zbytek3 >= 1 and zbytek4 >=1:
        pocet+=1
        print(i)
print(pocet,"prvocisel")
        
    


    