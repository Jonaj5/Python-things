class Vector():
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        return (self.x==other.x) and (self.y==other.y)
    
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    
    def __sub__(self,other):
        return Vector(self.x-other.x, self.y-other.y)
    
    def __mul__(self,other):
        return Vector(self.x*other.x, self.y*other.y)

v1=Vector(5,4)
v2=Vector(6,3)

print(v1+v2)