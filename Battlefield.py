from Fleet import Fleet
from Herd import Herd


class Battlefield:
    def __init__ (self):
        self.fleet = Fleet()
        self.herd = Herd()
        pass

    def fight(self): 
        self.herd.dinosaurs[0].attack(self.fleet.robots[0])
        self.fleet.robots[0].attack(self.herd.dinosaurs[0])
        
        # after an attack, if one getting attacked has 0 health, remove them from their list.
        # continue looping as long as both lists have at least one thing in it

        #who goes first? I want dinosaurs to go first
        for health in :
            if health == 0:
                print("The game is over, the dinosaurs have won!")
                pass
