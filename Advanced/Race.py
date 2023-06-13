class Race():
    
    def __init__(self, discipline):
        
        self.discipline = discipline
        self.participants = []
        self.results = []
        self.judge = ""
        
    def __str__(self):
        return f"{self.discipline}, Judge: {self.judge}, Number of participants: {len(self.participants)}"
    
    def add_participant(self, name):
        if name not in self.participants:
            self.participants.append(name)
            self.results.append(0)
    
    def remove_paticipant(self, name):
        pass

class Person:
    
    def __init__(self, name):
        self.name = name
        
    def print_race_results(self, race):
        print(f"Discipline: {race.discipline}")
        print(f"Judge: {self.judge}")
        for i in range(0,len(race.participants)):
            print(f"{i+1}, {race.participants[i]}: {race.results}")
            
class Participant(Person):
    
    def __init__(self, name):
        super().__init__(name)
        
    def join_race(self, race):
        race.add_participant(self.name)
        
    def leave_race(self, race):
        race.remove_participant(self.name)