from Dinosaur import Dinosaur

class Herd:
    def __init__ (self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur_one=Dinosaur("Alice")
        self.dinosaurs.append(dinosaur_one)
        dinosaur_two=Dinosaur("Bonnie")
        self.dinosaurs.append(dinosaur_two)
        dinosaur_three=Dinosaur("Clara")
        self.dinosaurs.append(dinosaur_three)



