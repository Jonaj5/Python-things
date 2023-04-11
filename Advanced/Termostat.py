class Termostat():

    ID=0
    
    def __init__(self, min, max):
        Termostat.ID +=1
        self.ID = Termostat.ID
        self.min = min
        self.max = max
        self.actual = min
        
    def __str__(self):
        return f"Aktuální teplota - {self.actual}, Rozsah {self.min} - {self.max}"
    
    def nastav(self, t):
        h=int(t)
        if h>=self.min and h<=self.max:
            self.actual = h
        else:
            self.actual = self.actual
        return f"Teplota nastavena - {self.actual}"


class Ovladac():
        
    def up(self, Termostat, hodnota):
        if hodnota>0 and hodnota<10:
            Termostat.actual = hodnota+Termostat.actual
        return f"Teplota zvýšena o {hodnota}"
    
    def down(self, hodnota, Termostat):
        if hodnota<0 and hodnota>-10:
          Termostat.actual = hodnota+Termostat.actual
        return f"Teplota snížena o {hodnota}"
        

t1 = Termostat(16, 30)
o1 = Ovladac()   
print(t1)
print(t1.nastav(input()))
print(o1.up(t1, 5))
print(t1)