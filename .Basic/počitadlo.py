text=input("Zadej text")
p=0

for i in text:
    if i not in".!?, ":
        p=p+1

print(p)