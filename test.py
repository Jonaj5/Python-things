class Student():
    
    ID = 1
    
    def __init__(self, jmeno, prijmeni, vek, trida):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.trida = trida
        self.id = Student.ID
        Student.ID += 1
    
    def __str__(self):
        return f"{self.id}. Jmenuji se {self.jmeno} {self.prijmeni}, je mi {self.vek} a chodím do {self.trida}"
    
    def __eq__(self, other):
        return self.vek == other.vek
    
    @property
    def email(self):
        return f"{self.jmeno}.{self.prijmeni}@spse.cz"
    
s1 = Student("Jan", "Pavlík", 17, "2.B")
s2 = Student("Petr", "Bednařík", 17, "2.B")
s3 = Student("Petr", "Horák", 18, "2.A")

print(s1)
print(s1.email)
print(s2)
print(s2.email)
print(s3)
print(s3.email)
print(s1 == s2)
print(s1 == s3)
