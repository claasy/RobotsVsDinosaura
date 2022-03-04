from Fleet import Fleet
from Herd import Herd

class Battlefield:
    def __init__ (self):
        self.fleet = Fleet()
        self.herd = Herd()
        pass
    def fight(self):        
        while(self.fleet.robots != [] and self.herd.dinosaurs != []):
            self.herd.dinosaurs[0].attack(self.fleet.robots[0])
            self.fleet.robots[0].attack(self.herd.dinosaurs[0])
            if (self.fleet.robots[0].health <= 0):
                self.fleet.robots.remove(self.fleet.robots[0])
            if (self.herd.dinosaurs[0].health <= 0):
                self.herd.dinosaurs.remove(self.herd.dinosaurs[0])    
        if (self.fleet.robots == []):
            print ("Dinosaurs won - Game over!")
        elif (self.herd.dinosaurs == []):
            print ("Robots won - Game over!")