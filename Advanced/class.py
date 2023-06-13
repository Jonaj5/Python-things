class Zamestnanec:
    
    rust_platu = 1.04
    poitadlo=0
    min_delka_hesla=6
    
    def __init__(self, jmeno, prijm, plat):
        self.jmeno = jmeno
        self.prijm = prijm
        self.plat  = plat
        
    def __str__(self):
        return f"{self.cele_jmeno()} - {self.email} - {self.plat}"
    
    def __add__(self, other):
        return self.plat + other.plat
    
    def __eq__(self, other):
        return self.plat == other.plat
        
    def cele_jmeno(self):
        return f'{self.jmeno} {self.prijm}'
    
    def zadost_o_rust_platu(self):
        self.plat = int(self.plat * self.rust_platu)
        
    @property
    def email(self):
        return f"{self.jmeno}.{self.prijm}@firma.cz"
    
    @email.setter
    def email(self, text):
        jmeno, prijm = text.split
        self.jmeno = jmeno
        self.prijm = prijm
    
    @classmethod
    def nastav_rust_platu(cls, rust):
        cls.rust_platu=rust
        
    @staticmethod
    def zvaliduj_heslo(heslo):
        return len(heslo)>=Zamestnanec.min_delka_hesla
    
    
class Developer(Zamestnanec):
    
    def __init__(self, jmeno, prijm, plat, jazyk):
        super().__init__(jmeno, prijm, plat)
        self.jazyk = jazyk
        
    def __str__(self):
        return f"{self.cele_jmeno()} - {self.email} - {self.jazyk} - {self.plat}"
    

class Manager(Zamestnanec):
    
    def __init__(self, jmeno, prijm, plat, employees=0):
        super().__init__(jmeno, prijm, plat)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
        
    
z1 = Zamestnanec('Jan', 'Sedlák', 30000)
z2 = Zamestnanec('Pan', 'Tedlák', 30000)
d1 = Developer("Pavel", "Kovář", 60000, "Python")

print(d1)