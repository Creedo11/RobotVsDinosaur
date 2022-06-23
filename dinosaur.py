

class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    
    def attack(self, robot):
        robot.health -= self.attack_power
        if robot.health <= 0:
            robot.health = 0
            print (f"Dinosaur {self.name} attacked {robot.name} for {self.attack_power} damage. {robot.name} has {robot.health} health remaining.")
            print(" ")
