class Dice():
    
    def __init__(self, pocet = 6):
        self.pocet_stran = pocet
        
    def roll(self):
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
        return f"[ {'♥'*pocet}{'♡'*(20-pocet)} ]"
    
    def Defend(self, hit):
        damage = hit-(self.defence+self.dice.roll())
        if damage>0:
            self.vitality -= damage
            print(f"{self.name} got damage {damage}")
            print(f"{self.name}:")
            print(f"HP - {self.vitality_graf()}")
            if not self.is_alive():
                print(f"{self.name} was DEFEATED")
        else:
            print(f"{self.name} defended him self")
            print(f"{self.name}:")
            print(f"HP - {self.vitality_graf()}")
                
    def Attack(self, opponent):
        hit = self.attack + self.dice.roll()
        print(f"\n{self.name} is attacking {hit}")
        opponent.Defend(hit)
    
class Mage(Warior):
    
    def __init__(self, name, vitality, attack, defence, dice, mana=0):
        super().__init__(name, vitality, attack, defence, dice)
        self.mana = mana
        self.max_mana = 100
        
    def mana_graf(self):
        pocet = int(self.mana/self.max_mana*100)
        return f"[ {'♥'*pocet}{'♡'*(20-pocet)} ]"
    
    def Defend(self, hit):
        damage = hit-(self.defence+self.dice.roll())
        if damage>0:
            self.vitality -= damage
            print(f"{self.name} got damage {damage}")
            print(f"{self.name}:")
            print(f"HP - {self.vitality_graf()}")
            if not self.is_alive():
                print(f"{self.name} was DEFEATED")
        else:
            print(f"{self.name} defended him self")
            print(f"{self.name}:")
            print(f"HP - {self.vitality_graf()}")
        
    def Attack(self, opponent):
        if self.mana > 100:
            hit = 2*self.attack + self.dice.roll()
            print(f"\n{self.name} attacks by magic ball {hit}")
            opponent.Defend(hit)
        
        else:
            hit = self.attack + self.dice.roll()
            print(f"\n{self.name} is attacking {hit}")
            opponent.Defend(hit)
            self.mana += 4*self.dice.roll()


k = Dice()
w = Warior("Cesar", 20, 20, 11, k)
m = Mage("Gandalf", 30, 5, 20, k)

while w.vitality > 0:
    w.Attack(m)
