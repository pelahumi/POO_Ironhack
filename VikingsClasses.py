import random

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

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

        if self.health != 0:
            return "A Saxon has received {} points of damage".format(damage)
        
        else:
            return "A Saxon has died in combat"

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
        return None
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        return None
        
    def vikingAttack(self):
        saxon = Saxon(random.choice(self.saxonArmy))
        viking = Viking(random.choice(self.vikingArmy))
        saxon.receiveDamage(viking.strength)
        if saxon.health == 0:
            self.saxonArmy.remove(saxon)
        else:
            return "A Saxon has received {} of damage".format(viking.strength)
        
    def saxonAttack(self):
        viking = Viking(random.choice(self.vikingArmy))
        saxon = Saxon(random.choice(self.saxonArmy))
        viking.receiveDamage(saxon.strength)
        if viking.health == 0:
            self.vikingArmy.remove(viking)
        else:
            return "{} has received {} of damage".format(viking.name, saxon.strength)

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day.."
        elif len(self.saxonArmy) == 1 and len(self.vikingArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle"
        

        


        