a=int(input("Zapiš sumu"))

print(f"{a//1000} * 1000")
b=a%1000

print(f"{b//500} * 500")
c=b%500

print(f"{c//100} * 100")
d=c%100

print(f"{d//50} * 50")
e=d%50

print(f"{e//10} * 10")
f=e%10

print(f"{f//5} * 5")
g=f%5

print(f"{g//1} * 1")
