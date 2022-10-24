class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health - damage

        if self.health != 0:
            return "{} has received {} points of damage".format(self.name, damage)
        
        else:
            return "{} has died in act of combat".format(self.name)
    
    def battleCry():
        return "Odin Owns You All!"


