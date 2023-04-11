class Dice():
    
    def __init__(self, pocet = 6):
        self.pocet_stran = pocet
        
    def hod(self):
        from random import randrange
        
        return randrange(1, self.pocet_stran)
    
    
class Warior():
    
    def __init__(self, name, vitality, attack, defence, dice):
        self.name = name
        self.vitality = vitality
        self.max_vitality = vitality
        self.attack = attack
        self.defence = defence
        self.dice = dice
    
    def __str__(self):
        return f"{self.name}"
    
    def is_alive(self):
        return self.vitality > 0
    
    def vitality_graf(self):
        pocet = int(self.vitality/self.max_vitality*20)
        if pocet == 0 and self.is_alive():
            pocet=1
        return f"[ {'♥'*pocet}{'⊠'*(20-pocet)} ]"
    

  
k = Dice()
w = Warior("HP", 20, 10, 11, k)
print(w.vitality_graf())

