from Robot import Robot

class Fleet:
    def __init__ (self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_one=Robot("Alan")
        self.robots.append(robot_one)
        robot_two=Robot("Bob")
        self.robots.append(robot_two)
        robot_three=Robot("Charlie")
        self.robots.append(robot_three)



    