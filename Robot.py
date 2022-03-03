from Weapon import Weapon


class Robot:
    def __init__ (self):
        self.name: ""
        self.health: int
        self.weapon: Weapon
    
    def set_name(self):
        self.name = Billy
        print ("Robot name:", self.name)