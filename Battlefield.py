from Fleet import Fleet
from Herd import Herd


class Battlefield:
    def __init__ (self):
        self.fleet = Fleet()
        self.herd = Herd()
        pass

    def run(self):
        pass

    #self.fleet[0].attack(self.herd[0])
    #self.herd[0].attack(self.fleet[0])