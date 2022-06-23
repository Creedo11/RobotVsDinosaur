from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Ultra Beam", 35)


    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        if dinosaur.health <= 0:
            dinosaur.health = 0
        print (f"Robot {self.name} attacked {dinosaur.name} for {self.active_weapon.attack_power} damage. {dinosaur.name} has {dinosaur.health} health remaining.")
        print(" ")


